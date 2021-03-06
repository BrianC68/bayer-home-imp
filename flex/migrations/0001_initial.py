# Generated by Django 3.0.4 on 2020-05-06 17:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display.', required=True)), ('text_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Align to left side of page.'), ('center', 'Align in center of page.'), ('right', 'Align to right side of page.')], help_text='Align the Title to the left, center or right side of the page.'))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title text for this card. Max length is 50 chars.', max_length=50)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 chars.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped to 500px by 300px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More...', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be cropped to 786px by 552px.')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image to the Left'), ('right', 'Image to the Right')], help_text='Image on the left with text on the right or image on the left with text on the right.')), ('title', wagtail.core.blocks.CharBlock(help_text='Title with max length of 60 chars.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More...', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length of 200 chars.', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More...', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('richtext', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'], template='streams/simple_richtext_block.html'))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
