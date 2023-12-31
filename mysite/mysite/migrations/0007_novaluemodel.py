# Generated by Django 4.1.3 on 2023-07-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0006_signupmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="NoValueModel",
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
                (
                    "digit_field",
                    models.IntegerField(
                        choices=[
                            (0, "0"),
                            (1, "1"),
                            (2, "2"),
                            (3, "3"),
                            (4, "4"),
                            (5, "5"),
                        ]
                    ),
                ),
                ("form_value", models.CharField(default="novalue", max_length=100)),
            ],
        ),
    ]
