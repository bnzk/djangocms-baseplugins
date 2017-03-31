# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('textimage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textimage',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='text', blank=True),
        ),
    ]
