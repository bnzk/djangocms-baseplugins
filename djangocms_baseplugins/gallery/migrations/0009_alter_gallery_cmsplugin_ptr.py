# Generated by Django 4.2.16 on 2024-11-13 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("gallery", "0008_auto_20230501_1509"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
    ]
