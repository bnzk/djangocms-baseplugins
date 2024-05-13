# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-08-05 16:40
from __future__ import unicode_literals

import django.db.models.deletion
import filer_addons.filer_gui.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0016_auto_20160608_1535"),
        ("filer", "0010_auto_20180414_2058"),
    ]

    operations = [
        migrations.CreateModel(
            name="InlineDownload",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="inline_download_inlinedownload",
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
                (
                    "height",
                    models.CharField(
                        blank=True, default="", max_length=32, verbose_name="Height"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="InlineDownloadEntry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link_text", models.CharField(blank=True, default="", max_length=255)),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "file",
                    filer_addons.filer_gui.fields.FilerFileField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="inline_download_inlinedownloadentry_download",
                        to="filer.File",
                        verbose_name="Download",
                    ),
                ),
                (
                    "inline_downloads",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="downloads",
                        to="inline_download.InlineDownload",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]
