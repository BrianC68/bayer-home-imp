# Generated by Django 3.0.4 on 2020-05-05 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('gallery', '0002_auto_20200505_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypage',
            name='gallery_listing_page_image',
            field=models.ForeignKey(help_text='Image from this collection that will appear on Gallery Listing Page. Image will be cropped to 500px by 300px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='gallerypage',
            name='gallery_collection',
            field=models.ForeignKey(help_text='Choose the image gallery you created in "Settings - Collections".', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Collection'),
        ),
    ]
