# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=models.CASCADE, parent_link=True,
                                                       related_name='text_text', auto_created=True,
                                                       primary_key=True, serialize=False,
                                                       to='cms.CMSPlugin')),
                ('title', models.CharField(default='', max_length=256, blank=True)),
                ('published', models.BooleanField(default=True)),
                ('in_menu', models.BooleanField(default=False)),
                ('layout', models.CharField(default='', max_length=64)),
                ('background', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('anchor', models.SlugField(default='', blank=True)),
                ('body', ckeditor.fields.RichTextField(verbose_name='text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
    ]
