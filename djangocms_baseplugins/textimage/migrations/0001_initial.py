# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
import filer.fields.image
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0016_auto_20160608_1535"),
        ("filer", "0006_auto_20160623_1627"),
    ]

    operations = [
        migrations.CreateModel(
            name="TextImage",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        parent_link=True,
                        on_delete=models.CASCADE,
                        related_name="textimage_textimage",
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("title", models.CharField(default="", max_length=256, blank=True)),
                ("published", models.BooleanField(default=True)),
                ("in_menu", models.BooleanField(default=False)),
                ("layout", models.CharField(default="", max_length=64)),
                ("background", models.CharField(default="", max_length=64)),
                ("color", models.CharField(default="", max_length=64)),
                ("anchor", models.SlugField(default="", blank=True)),
                ("caption", models.CharField(default="", max_length=255, blank=True)),
                ("alt_text", models.CharField(default="", max_length=255, blank=True)),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        on_delete=django.db.models.deletion.SET_NULL,
                        verbose_name="image",
                        to="filer.Image",
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin", models.Model),
        ),
    ]
