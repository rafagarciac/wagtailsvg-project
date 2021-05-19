from django.db import models
from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class HomePage(Page):
    pass
exit

class TestPage(Page):
    logo = models.ForeignKey(
        Svg,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    body = StreamField([
        ('svg', SvgChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        SvgChooserPanel('logo'),
        StreamFieldPanel('body'),
    ]