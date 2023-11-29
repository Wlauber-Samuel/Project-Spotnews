# Generated by Django 4.2.3 on 2023-11-29 20:23

from django.db import migrations, models

import news.models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(
                    max_length=200, validators=[news.models.validate_title])),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(blank=True, upload_to="img/")),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="news", to="news.category"
                    ),
                ),
            ],
        ),
    ]
