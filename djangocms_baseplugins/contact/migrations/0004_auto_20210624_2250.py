# Generated by Django 2.2.20 on 2021-06-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0003_auto_20181024_1352"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="custom",
            field=models.CharField(
                blank=True, default="", max_length=128, verbose_name="Custom"
            ),
        ),
        migrations.AddField(
            model_name="contact",
            name="size",
            field=models.CharField(
                blank=True, default="", max_length=64, verbose_name="Size"
            ),
        ),
    ]
