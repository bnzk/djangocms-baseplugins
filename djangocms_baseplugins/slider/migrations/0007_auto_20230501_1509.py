# Generated by Django 2.2.28 on 2023-05-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0006_auto_20210624_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='custom',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Custom'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='size',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Size'),
        ),
    ]
