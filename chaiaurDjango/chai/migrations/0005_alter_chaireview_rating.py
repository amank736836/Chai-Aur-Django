# Generated by Django 5.1.7 on 2025-03-19 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chai", "0004_rename_store_chaistore_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chaireview",
            name="rating",
            field=models.CharField(
                choices=[
                    (1, "1 Star"),
                    (2, "2 Star"),
                    (3, "3 Star"),
                    (4, "4 Star"),
                    (5, "5 Star"),
                ],
                max_length=1,
            ),
        ),
    ]
