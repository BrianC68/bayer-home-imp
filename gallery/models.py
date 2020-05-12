from django.db import models
from django_extensions.db.fields import AutoSlugField

from wagtail.core.models import Collection, Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

# COLLECTION_CHOICES = ((c.id, c.name) for c in Collection.objects.all())


class GalleryListingPage(Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['gallery.GalleryPage']
    max_count = 1
    template = 'gallery/gallery_listing_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['galleries'] = GalleryPage.objects.live().public()
        return context

   
class GalleryPage(Page):

    parent_page_types = ['gallery.GalleryListingPage']
    subpage_types = []
    template = 'gallery/gallery_page.html'

    # Model Fields

    gallery_description = models.CharField(
        blank=True,
        max_length=250,
        help_text='Short description of the job related to the gallery collection, max 250 Chars.'
    )

    gallery_listing_page_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Image from this collection that will appear on Gallery Listing Page. Image will be cropped to 1000px by 600px.',
        on_delete=models.SET_NULL
    )

    gallery_collection = models.ForeignKey(
        'wagtailcore.Collection',
        # choices=COLLECTION_CHOICES,
        blank=False,
        null=True,
        related_name='+',
        help_text='Choose the image gallery you created in "Settings - Collections".',
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        FieldPanel('gallery_description'),
        FieldPanel('gallery_collection'),
        ImageChooserPanel('gallery_listing_page_image')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['images'] = Image.objects.filter(collection=self.gallery_collection)
        return context
