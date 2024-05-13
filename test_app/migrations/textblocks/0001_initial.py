# Generated by Django 2.2.20 on 2021-04-13 12:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TextBlock",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        db_index=True, max_length=120, unique=True, verbose_name="key"
                    ),
                ),
                (
                    "help_text",
                    models.CharField(
                        default="", max_length=255, verbose_name="help text"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("text/plain", "text/plain"),
                            ("text/html", "text/html"),
                        ],
                        max_length=20,
                        verbose_name="type",
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, default="", verbose_name="content"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created at"
                    ),
                ),
                (
                    "accessed_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="last access"
                    ),
                ),
            ],
        ),
    ]
