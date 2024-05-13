# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-24 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="geo_error",
            field=models.BooleanField(
                default=False, verbose_name="Probleme mit der Adresse?"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="lat",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="lng",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
