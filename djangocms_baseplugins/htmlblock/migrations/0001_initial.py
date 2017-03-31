# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlBlock',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='htmlblock_htmlblock', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='', max_length=256, blank=True)),
                ('published', models.BooleanField(default=True)),
                ('in_menu', models.BooleanField(default=False)),
                ('layout', models.CharField(default='', max_length=64)),
                ('background', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('anchor', models.SlugField(default='', blank=True)),
                ('html_block', models.TextField(help_text='Use with caution.', verbose_name='Html Block')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
