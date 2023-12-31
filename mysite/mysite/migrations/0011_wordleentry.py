# Generated by Django 4.2.1 on 2023-08-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0010_alter_novaluemodel_catchphrase_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WordleEntry",
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
                ("letter_1", models.CharField(max_length=1)),
                ("letter_2", models.CharField(max_length=1)),
                ("letter_3", models.CharField(max_length=1)),
                ("letter_4", models.CharField(max_length=1)),
                ("letter_5", models.CharField(max_length=1)),
                ("image_data", models.TextField()),
            ],
        ),
    ]
