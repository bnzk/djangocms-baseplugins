# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
import filer.fields.image
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("image", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=filer.fields.image.FilerImageField(
                related_name="image_image_image",
                on_delete=django.db.models.deletion.SET_NULL,
                verbose_name="image",
                to="filer.Image",
                null=True,
            ),
        ),
    ]
