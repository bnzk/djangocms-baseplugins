# Generated by Django 2.2.28 on 2023-05-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0003_auto_20210624_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='custom',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Custom'),
        ),
        migrations.AlterField(
            model_name='download',
            name='size',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='downloadsection',
            name='custom',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='Custom'),
        ),
        migrations.AlterField(
            model_name='downloadsection',
            name='size',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Size'),
        ),
    ]