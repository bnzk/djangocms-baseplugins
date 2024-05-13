# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-13 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0008_auto_20190923_1628"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="autoplay",
            field=models.BooleanField(
                default=False,
                help_text="Enforces muting the video!",
                verbose_name="Autoplay",
            ),
        ),
    ]
