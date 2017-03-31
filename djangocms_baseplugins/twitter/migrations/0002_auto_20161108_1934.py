# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetEmbed',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='twitter_tweetembed', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='', max_length=256, blank=True)),
                ('published', models.BooleanField(default=True)),
                ('in_menu', models.BooleanField(default=False)),
                ('layout', models.CharField(default='', max_length=64)),
                ('background', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('anchor', models.SlugField(default='', blank=True)),
                ('tweet_url', models.URLField(help_text='Example: https://twitter.com/MdDoomFest/status/795834590481018880', verbose_name='Tweet URL')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='twitter',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='Twitter',
        ),
    ]
