# Generated by Django 4.1 on 2022-08-05 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tags",
            new_name="Tag",
        ),
    ]
