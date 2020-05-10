from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks as wagtail_blocks

from streams import blocks


class HomePage(Page):
    
    parent_page_types = ['wagtailcore.Page']
    subpage_types = ['flex.FlexPage', 'services.ServiceListingPage', 'contact.ContactPage', 'gallery.GalleryListingPage']
    max_count = 1
    lead_text = models.CharField(
        max_length=250, 
        blank=True,
        help_text='Subheading text under the banner title, 250 Chars max length.'
    )

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page link.',
        on_delete=models.SET_NULL
    )
    button_text = models.CharField(
        max_length=50,
        default='Read More...',
        blank=False,
        help_text='Text shown on the button, 50 Chars max length.'
    )
    body = StreamField([
        ('title', blocks.TitleBlock()),
        ('cards', blocks.CardsBlock()),
        ('image_and_text', blocks.ImageAndTextBlock()),
        ('cta', blocks.CallToActionBlock()),
        ('richtext', wagtail_blocks.RichTextBlock(
            template='streams/simple_richtext_block.html',
            features=['h2', 'h3', 'bold', 'italic', 
                    'ol', 'ul', 'hr', 'link', 
                    'document-link', 'image']
        )),
        ], null=True, blank=True
        )
    

    content_panels = Page.content_panels + [
        FieldPanel('lead_text'),
        FieldPanel('button_text'),
        PageChooserPanel('button'),
        StreamFieldPanel('body'),
    ]
