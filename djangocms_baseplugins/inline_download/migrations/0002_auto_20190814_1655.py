# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-14 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("inline_download", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inlinedownloadentry",
            old_name="inline_downloads",
            new_name="inline_download",
        ),
    ]
