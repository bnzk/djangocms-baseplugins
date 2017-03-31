# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlblock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='htmlblock',
            old_name='html_block',
            new_name='htmlblock',
        ),
    ]
