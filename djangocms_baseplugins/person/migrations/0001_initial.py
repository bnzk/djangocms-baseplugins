# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, on_delete=models.CASCADE,related_name='person_person', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='', max_length=256, blank=True)),
                ('published', models.BooleanField(default=True)),
                ('in_menu', models.BooleanField(default=False)),
                ('layout', models.CharField(default='', max_length=64)),
                ('background', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('anchor', models.SlugField(default='', blank=True)),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='last name')),
                ('body', ckeditor.fields.RichTextField(default='', verbose_name='text', blank=True)),
                ('email', models.EmailField(default='', max_length=254, verbose_name='email', blank=True)),
                ('website', models.URLField(default='', verbose_name='website', blank=True)),
                ('phone', models.CharField(default='', max_length='32', verbose_name='phone', blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PersonSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, on_delete=models.CASCADE,related_name='person_personsection', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='', max_length=256, blank=True)),
                ('published', models.BooleanField(default=True)),
                ('in_menu', models.BooleanField(default=False)),
                ('layout', models.CharField(default='', max_length=64)),
                ('background', models.CharField(default='', max_length=64)),
                ('color', models.CharField(default='', max_length=64)),
                ('anchor', models.SlugField(default='', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
