# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_audit_trail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagerecord',
            name='page_url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
