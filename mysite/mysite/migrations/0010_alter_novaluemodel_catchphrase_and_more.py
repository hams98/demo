# Generated by Django 4.2.1 on 2023-08-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0009_novaluemodel_catchphrase_novaluemodel_format_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="novaluemodel",
            name="catchphrase",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="novaluemodel",
            name="form_value",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="novaluemodel",
            name="format",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="novaluemodel",
            name="interests",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="valuemodel",
            name="catchphrase",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="valuemodel",
            name="form_value",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="valuemodel",
            name="interests",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="valuemodel",
            name="value_importance",
            field=models.CharField(max_length=200),
        ),
    ]