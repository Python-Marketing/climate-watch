from PIL import Image
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from api.models import *

from djangocms_blog.cms_appconfig import BlogConfig
from djangocms_blog.models import Post as BlogPost

from filer.models import ThumbnailOption
from django.conf import settings

from api.utils.page import create_new_page
from site_server.default_site import image_sizes


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write("Initialize CMS")
        # Adapting site settings
        self.stdout.write("Changing site details")
        do = Site.objects.all().count()
        if do == 1:
            site = Site.objects.get(id=1)
            site_name = getattr(settings, 'SITE_NAME', 'localhost')
            site_domain = getattr(settings, 'SITE_URL', 'http://127.0.0.1')
            site.name = site_name
            site.domain = site_domain
            site.save()
        # Add some image options
        do = ThumbnailOption.objects.all().count()
        if do == 0:
            for key, item in image_sizes.items():
                self.stdout.write("Adding image option {} : {} x {}".format(key, item['width'], item['height']))
                ThumbnailOption(
                    name=key,
                    width=item['width'],
                    height=item['height'],
                    crop=False,
                    upscale=False
                ).save()

        self.stdout.write("Site ready")

