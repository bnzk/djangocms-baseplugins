# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("slider", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="slider",
            name="anchor_de",
            field=models.SlugField(
                blank=True, default="", null=True, verbose_name="Anchor"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="anchor_en",
            field=models.SlugField(
                blank=True, default="", null=True, verbose_name="Anchor"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="anchor_fr",
            field=models.SlugField(
                blank=True, default="", null=True, verbose_name="Anchor"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="title_de",
            field=models.CharField(
                blank=True, default="", max_length=256, null=True, verbose_name="Title"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="title_en",
            field=models.CharField(
                blank=True, default="", max_length=256, null=True, verbose_name="Title"
            ),
        ),
        migrations.AddField(
            model_name="slider",
            name="title_fr",
            field=models.CharField(
                blank=True, default="", max_length=256, null=True, verbose_name="Title"
            ),
        ),
    ]
