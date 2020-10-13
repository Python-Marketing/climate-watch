import time
from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import HttpResponse
from django.utils.html import format_html
from django.views.generic import FormView
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.utils import json

from allauth.account import app_settings
from allauth.account.forms import LoginForm
from allauth.account.utils import passthrough_next_redirect_url, get_next_redirect_url
from allauth.account.views import sensitive_post_parameters_m, AjaxCapableProcessFormViewMixin, \
    RedirectAuthenticatedUserMixin
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_request_param, get_form_class
from cms.models import Page, reverse
from djangocms_blog.models import Post
from .models import Post as ApiPost, Volunteer
from .serializer import UserSerializer, PageSerializer, PostSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = ApiPost.objects.all()
    serializer_class = PostSerializer


# ViewSets define the view behavior.
class SearchViewSet(viewsets.ModelViewSet):
    queryset = ApiPost.objects.all()
    serializer_class = PostSerializer


class ClimateWatch(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        response = "No entry"

        import urllib.request
        import urllib.parse
        import json
        from datetime import date, datetime

        # read the string into a datetime object

        mapquestapi_key = "kwRexg4bqOtJGT6DFsibO8KHJVxYfenj"

        location = self.request.GET.get('location').strip().replace(" ", ",")

        # start_date = datetime.strptime(self.request.GET.get('start_date'), "%m/%d/%Y").timestamp()
        # end_date = datetime.strptime(self.request.GET.get('end_date'), "%m/%d/%Y").timestamp()
        #
        url = 'http://www.mapquestapi.com/geocoding/v1/address?key={}&location={}'.format(mapquestapi_key, location)
        f = urllib.request.urlopen(url).read().decode('utf-8')

        result = json.loads(f)
        no_locations = len(result['results'][0]['locations'])

        if no_locations > 1:
            message = "Please be more specific, to many locations found..."
            return HttpResponse(message, content_type='text/html', status=200)

        map = result['results'][0]['locations'][0]['mapUrl']
        lat = result['results'][0]['locations'][0]["displayLatLng"]["lat"]
        long = result['results'][0]['locations'][0]["displayLatLng"]["lng"]

        import requests
        key = "3b54bea1042da60ea275c9e518636242"
        url = "https://api.openweathermap.org/data/2.5/onecall"

        querystring = {
            # "type": "hour",
            "appid": key,
            # "start_time": start_date,
            # "end_time": end_date,
            "lat":lat,
            "lon":long,
            "units":"metric"
        }

        response = requests.request("GET", url, params=querystring)
        result = json.loads(response.text)
        last_2_days = result['hourly']
        last_week = result['daily']

        week_data = {
            'temp_min': [],
            'temp_max': [],
            'temp_average': [],
            'humidity': [],
            'dew_point': [],
            'wind_speed': [],
            'labels': [],
        }
        days_data = {
            'temp_data': [],
            'humidity': [],
            'dew_point': [],
            'wind_speed': [],
            'labels': [],
        }
        import statistics
        # computes min, max, average
        # and median temperature and humidity for that location
        # and period and returns that to the user
        humidity = 0
        for week in last_week:
            # get averge out of all of them

            week_data['temp_min'].append(week['temp']['min'])
            week_data['temp_max'].append(week['temp']['max'])
            week_data['humidity'].append(week['humidity'])
            week_data['dew_point'].append(week['dew_point'])
            week_data['wind_speed'].append(week['wind_speed'])
            week_data['labels'].append(time.strftime("%Y/%m/%d", time.localtime(week['dt'])))
            humidity += week['humidity']

        weekly_humidity = humidity / 8
            #time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(time.time()))
        for day in last_2_days:
            days_data['temp_data'].append(day['temp'])
            days_data['humidity'].append(day['humidity'])
            days_data['dew_point'].append(day['dew_point'])
            days_data['wind_speed'].append(day['wind_speed'])
            days_data['labels'].append(time.strftime("%Y/%m/%d", time.localtime(day['dt'])))

        n, average_humidity, average_temp = 0, [], []
        while n != 49:
            average_humidity.append(statistics.mean(days_data['humidity']))
            average_temp.append(statistics.mean(days_data['temp_data']))
            n += 1

        data = {
            "days_data": days_data,
            "week_data": week_data,
            "image_src":map,
            "weekly_humidity":weekly_humidity,
            "average_temp": statistics.mean(week_data['temp_min']),
            "average_daily_humidity": statistics.mean(days_data['humidity']),
            "average_daily_temp": statistics.mean(days_data['temp_data']),
            "chart_average_daily_humidity" :average_humidity,
            "chart_average_daily_temp":average_temp,
        }

        return HttpResponse(json.dumps(data), content_type='application/json', status=200)


class SocialLoginView(RedirectAuthenticatedUserMixin,
                      AjaxCapableProcessFormViewMixin,
                      FormView):
    form_class = LoginForm
    template_name = "account/social_login." + app_settings.TEMPLATE_EXTENSION
    success_url = None
    redirect_field_name = "next"

    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        return super(SocialLoginView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(SocialLoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_form_class(self):
        return get_form_class(app_settings.FORMS, 'login', self.form_class)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response

    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (get_next_redirect_url(
            self.request,
            self.redirect_field_name) or self.success_url)
        return ret

    def get_context_data(self, **kwargs):
        ret = super(SocialLoginView, self).get_context_data(**kwargs)
        signup_url = passthrough_next_redirect_url(self.request,
                                                   reverse("account_signup"),
                                                   self.redirect_field_name)
        redirect_field_value = get_request_param(self.request,
                                                 self.redirect_field_name)
        site = get_current_site(self.request)

        ret.update({"signup_url": signup_url,
                    "site": site,
                    "redirect_field_name": self.redirect_field_name,
                    "redirect_field_value": redirect_field_value})
        return ret


social_login = SocialLoginView.as_view()
