# Generated by Django 4.2.6 on 2023-10-25 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0019_remove_profile_value_importance"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WordleEntry",
        ),
    ]