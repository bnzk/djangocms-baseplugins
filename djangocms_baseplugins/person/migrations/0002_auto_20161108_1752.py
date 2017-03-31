# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='person_person_image', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image'),
        ),
    ]
