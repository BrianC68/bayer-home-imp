from django.db import models
from django.core.exceptions import ValidationError
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField


@register_setting
class FooterCTASettings(BaseSetting):

    title = models.TextField(blank=False, null=True)

    subtitle = models.TextField(blank=False, null=True)

    button_internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional internal page link.',
        on_delete=models.SET_NULL
    )

    button_text = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        help_text='30 Character Max.'
    )

    button_external_page = models.URLField(
        blank=True,
        null=True,
        help_text='Enter an external page url or choose an internal page link.'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        PageChooserPanel('button_internal_page'),
        FieldPanel('button_external_page'),
        FieldPanel('button_text')
    ]

    def save(self, *args, **kwargs):

        key = make_template_fragment_key('footer_cta_settings')
        cache.delete(key)
        return super().save(*args, **kwargs)

    def clean(self):

        if self.button_internal_page and self.button_external_page:
            error = 'You may only select an internal page OR and external URL!'
            raise ValidationError({
                'button_internal_page': ValidationError(error),
                'button_external_page': ValidationError(error)
            })

        if not self.button_internal_page and not self.button_external_page:
            error = 'You must link to an internal page OR provide an external page URL!'
            raise ValidationError({
                'button_internal_page': ValidationError(error),
                'button_external_page': ValidationError(error)
            })


@register_setting
class ContactSettings(BaseSetting):
    '''Contact phone number and email address.'''

    contact_phone = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        help_text='Enter an optional contact phone number.'
    )

    contact_email = models.EmailField(
        blank=True,
        null=True,
        help_text='Enter an optional contact email address.'
    )

    panels = [
        FieldPanel('contact_phone'),
        FieldPanel('contact_email')
    ]

def save(self, *args, **kwargs):

        key = make_template_fragment_key('footer_contact_settings')
        cache.delete(key)
        return super().save(*args, **kwargs)


@register_setting
class ServiceAreaSettings(BaseSetting):

    counties_served = models.TextField(
        blank=True,
        help_text='List of service area counties.'
    )


@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(
        blank=True,
        help_text='Enter Company Facebook URL',
    )

    youtube = models.URLField(
        blank=True,
        help_text='Enter Company YouTube URL',
    )

    instagram = models.URLField(
        blank=True,
        help_text='Enter Company Instagram URL',
    )

    twitter = models.URLField(
        blank=True,
        help_text='Enter Company Twitter URL',
    )

    linkedin = models.URLField(
        blank=True,
        help_text='Enter Company LinkedIn URL'
    )

    def save(self, *args, **kwargs):

        key = make_template_fragment_key('footer_social_settings')
        cache.delete(key)
        return super().save(*args, **kwargs)
