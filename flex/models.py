from django.db import models

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core import blocks as wagtail_blocks
from wagtail.images.blocks import ImageChooserBlock
from streams import blocks


class FlexPage(Page):

    parent_page_types = ['home.HomePage', 'flex.FlexPage']

    body = StreamField([
        ('title', blocks.TitleBlock()),
        ('cards', blocks.CardsBlock()),
        ('image_and_text', blocks.ImageAndTextBlock()),
        ('cta', blocks.CallToActionBlock()),
        # ('richtext_with_title', blocks.RichTextWithTitleBlock()), # Optional way of doing richtext
        ('richtext', wagtail_blocks.RichTextBlock(
            template='streams/simple_richtext_block.html',
            features=['h3', 'bold', 'italic', 
                    'ol', 'ul', 'hr', 'link', 
                    'document-link', 'image']
        )),
        ], null=True, blank=True
        )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    class Meta:
        verbose_name = 'Flex (misc) page'
        verbose_name_plural = 'Flex (misc) pages'
