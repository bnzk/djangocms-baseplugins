# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("textimage", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="textimage",
            name="body",
            field=ckeditor.fields.RichTextField(verbose_name="text", blank=True),
        ),
    ]
