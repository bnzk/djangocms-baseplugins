# Generated by Django 2.2.20 on 2021-06-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0009_auto_20191113_1057"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="custom",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="Custom"
            ),
        ),
        migrations.AddField(
            model_name="video",
            name="size",
            field=models.CharField(
                blank=True, default="", max_length=64, verbose_name="Size"
            ),
        ),
    ]
