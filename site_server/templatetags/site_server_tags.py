from django import template
from django.utils.html import format_html

from cms.models import Q
from djangocms_blog.models import Post


register = template.Library()


def query_lookup(query='', filter=[], pages=[]):
    results = []
    for q in query:
        for v in filter:
            if q.title.find(v) != -1 and v not in pages:
                results.append(q)
    return results


@register.simple_tag
def query_filter(request, query={}, value='', random=False, number=False):
    pages = []

    request.session['used_blogs'] = "Value"

    values = value.split(',')
    results = query_lookup(query, values, pages)

    if len(results) == 0:
        search = Q()
        for value in values:
            search.add(Q(translations__title__icontains=value), Q.OR)

        query = Post.objects.filter(search).exclude(publish=False).exclude(main_image__isnull=True)
        results = query_lookup(query, values)

    if number:
        return results[0]

    # if len(results) == 1:
    #     if value not in pages:
    #         return results[0]

    if random:
        try:
            import random
            results = random.choice(results)
        except:
            pass

    return results


