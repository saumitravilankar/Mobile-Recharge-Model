# Generated by Django 4.1.4 on 2022-12-18 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wallet",
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
                ("balance", models.PositiveIntegerField(default=50)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DebitCard",
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
                ("card_number", models.CharField(max_length=12, unique=True)),
                ("balance", models.PositiveIntegerField(default=10000)),
                (
                    "expiration_date",
                    models.IntegerField(
                        choices=[
                            (2017, "2017"),
                            (2018, "2018"),
                            (2019, "2019"),
                            (2020, "2020"),
                            (2021, "2021"),
                            (2022, "2022"),
                            (2023, "2023"),
                            (2024, "2024"),
                            (2025, "2025"),
                            (2026, "2026"),
                            (2027, "2027"),
                            (2028, "2028"),
                            (2029, "2029"),
                            (2030, "2030"),
                        ]
                    ),
                ),
                ("cvv", models.CharField(max_length=3)),
                ("card_owner", models.CharField(max_length=500, null=True)),
                ("card_added", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
