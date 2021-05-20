import os
import urllib.parse

from django import template
from django.conf import settings

from wagtail.images.models import get_upload_to

register = template.Library()


@register.filter
def svg_url(rendition):
    file = rendition.file
    filename = file.name.split("/")[1].split(".")[0]
    svg_file = "{}.{}".format(filename, "svg")
    url = settings.MEDIA_SVG_URL + svg_file
    return urllib.parse.urljoin(settings.MEDIA_URL, url)
