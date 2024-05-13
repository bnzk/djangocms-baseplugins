# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 08:46
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0016_auto_20160608_1535"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeaserSection",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="teaser_section_teasersection",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, default="", max_length=256, verbose_name="Title"
                    ),
                ),
                (
                    "published",
                    models.BooleanField(default=True, verbose_name="Published?"),
                ),
                (
                    "published_from_date",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Published from",
                    ),
                ),
                (
                    "published_until_date",
                    models.DateTimeField(
                        blank=True,
                        default=None,
                        null=True,
                        verbose_name="Published until",
                    ),
                ),
                (
                    "in_menu",
                    models.BooleanField(default=False, verbose_name="In Menu?"),
                ),
                (
                    "layout",
                    models.CharField(
                        blank=True, default="", max_length=64, verbose_name="Layout"
                    ),
                ),
                (
                    "background",
                    models.CharField(
                        blank=True, default="", max_length=64, verbose_name="Background"
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, default="", max_length=64, verbose_name="Color"
                    ),
                ),
                (
                    "anchor",
                    models.SlugField(blank=True, default="", verbose_name="Anchor"),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
