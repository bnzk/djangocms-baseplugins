# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-04 06:07
from __future__ import unicode_literals

import django.db.models.deletion
import filer.fields.image
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image", "0002_auto_20161108_1852"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="background",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
        migrations.AlterField(
            model_name="image",
            name="color",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=filer.fields.image.FilerImageField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="image_image_image",
                to="filer.Image",
                verbose_name="Image",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="layout",
            field=models.CharField(blank=True, default="", max_length=64),
        ),
    ]
