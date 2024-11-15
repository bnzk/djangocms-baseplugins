# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-22 12:37
from __future__ import unicode_literals

import django.db.models.deletion
import filer_addons.filer_gui.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inline_gallery", "0002_auto_20180816_1245"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inlinegalleryimage",
            name="gallery",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="inline_gallery.InlineGallery",
            ),
        ),
        migrations.AlterField(
            model_name="inlinegalleryimage",
            name="image",
            field=filer_addons.filer_gui.fields.FilerImageField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="inline_gallery_inlinegalleryimage_image",
                to=settings.FILER_IMAGE_MODEL,
                verbose_name="Image",
            ),
        ),
    ]
