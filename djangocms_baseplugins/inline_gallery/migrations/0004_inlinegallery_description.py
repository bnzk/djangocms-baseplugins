# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-14 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inline_gallery', '0003_auto_20180822_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlinegallery',
            name='description',
            field=models.TextField(blank=True, default=b''),
        ),
    ]