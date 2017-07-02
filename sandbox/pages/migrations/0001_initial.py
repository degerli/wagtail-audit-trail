# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 06:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
