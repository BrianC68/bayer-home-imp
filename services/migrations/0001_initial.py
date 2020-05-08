# Generated by Django 3.0.4 on 2020-04-30 16:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('subtitle', models.CharField(blank=True, help_text='Description on service listing page, 500 Chars max length.', max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('card_description', models.CharField(blank=True, help_text='Short description of service for display on services page, 200 Chars max length.', max_length=200)),
                ('description', wagtail.core.fields.RichTextField(help_text='Full description of the service.', null=True)),
                ('button_text', models.CharField(blank=True, default='Back to Services', help_text='Button text for internal page link, max length 50 Chars.', max_length=50)),
                ('internal_page', models.ForeignKey(blank=True, help_text='Select an internal Wagtail page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('service_image', models.ForeignKey(help_text='This image will be used on the Service listing page and will be cropped                 to 500px by 300px on this page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
