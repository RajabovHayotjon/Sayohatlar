# Generated by Django 5.0.6 on 2024-07-18 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0013_tour_price_list_tour_programm_tour_visa"),
    ]

    operations = [
        migrations.CreateModel(
            name="TourReview",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("rating", models.PositiveSmallIntegerField(default=1)),
                ("body", models.TextField()),
                (
                    "tour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="tours.tour",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
