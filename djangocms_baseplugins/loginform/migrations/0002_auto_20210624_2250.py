# Generated by Django 2.2.20 on 2021-06-24 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginform',
            name='custom',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Custom'),
        ),
        migrations.AddField(
            model_name='loginform',
            name='size',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Size'),
        ),
    ]
