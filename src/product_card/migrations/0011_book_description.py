# Generated by Django 4.1.1 on 2022-11-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_card", "0010_alter_book_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
