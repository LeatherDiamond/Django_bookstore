# Generated by Django 4.1.1 on 2022-10-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookAuthor",
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
                ("name", models.CharField(max_length=30)),
                ("surname", models.CharField(max_length=30)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
