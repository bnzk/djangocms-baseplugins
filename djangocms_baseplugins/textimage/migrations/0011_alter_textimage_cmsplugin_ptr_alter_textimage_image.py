# Generated by Django 4.2.16 on 2024-11-13 13:32

import django.db.models.deletion
import filer_addons.filer_gui.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ("textimage", "0010_auto_20230501_1509"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textimage",
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
        migrations.AlterField(
            model_name="textimage",
            name="image",
            field=filer_addons.filer_gui.fields.FilerImageField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_image",
                to=settings.FILER_IMAGE_MODEL,
                verbose_name="Image",
            ),
        ),
    ]
