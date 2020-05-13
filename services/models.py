from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField


class ServiceListingPage(Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['services.ServicePage']
    max_count = 1
    template = 'services/service_listing_page.html'
    
    # Model Fields
    subtitle = models.CharField(
        max_length=500,
        blank=True,
        help_text='Description on service listing page, 500 Chars max length.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] = ServicePage.objects.live().public()
        return context


class ServicePage(Page):

    parent_page_types = ['services.ServiceListingPage']
    subpage_types = []
    template = 'services/service_page.html'

    # Model Fields
    card_description = models.CharField(
        blank=True,
        max_length=200,
        help_text='Short description of service for display on services page, 200 Chars max length.'
    )
    description = RichTextField(
        blank=False,
        null=True,
        features=['h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link'],
        help_text='Full description of the service.'
    )
    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='This image will be used on the Service listing page and will be cropped \
                to 500px by 300px on this page.',
        related_name='+',
    )
    button_text = models.CharField(
        max_length=50,
        default='Back to Services',
        blank=True,
        help_text='Button text for internal page link, max length 50 Chars.'
    )
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an internal Wagtail page',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel('card_description'),
        FieldPanel('description'),
        ImageChooserPanel('service_image'),
        FieldPanel('button_text'),
        PageChooserPanel('internal_page')
    ]

    def save(self, *args, **kwargs):

        key = make_template_fragment_key('service_listing')
        cache.delete(key)
        return super().save(*args, **kwargs)
    