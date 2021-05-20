import os
import urllib.parse

from django import template
from django.conf import settings

from wagtail.images.models import get_upload_to

register = template.Library()

SVG_MEDIA_URL = "svgs/"


@register.filter
def svg_url(rendition):
    svg_extension = "svg"
    image = rendition.image
    pre, _ = os.path.splitext(image.title)
    svg_file = "{}.{}".format(pre, svg_extension)
    url = SVG_MEDIA_URL + svg_file
    return urllib.parse.urljoin(settings.MEDIA_URL, url)
