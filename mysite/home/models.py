from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.models import Image
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    pass


class TestPage(Page):
    logo = models.ForeignKey(
        Image, related_name="+", null=True, blank=True, on_delete=models.SET_NULL
    )
    body = StreamField(
        [
            ("svg", ImageChooserBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("logo"),
        StreamFieldPanel("body"),
    ]
