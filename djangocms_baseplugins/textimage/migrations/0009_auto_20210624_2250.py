# Generated by Django 2.2.20 on 2021-06-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("textimage", "0008_auto_20180822_1237"),
    ]

    operations = [
        migrations.AddField(
            model_name="textimage",
            name="custom",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="Custom"
            ),
        ),
        migrations.AddField(
            model_name="textimage",
            name="size",
            field=models.CharField(
                blank=True, default="", max_length=64, verbose_name="Size"
            ),
        ),
    ]
