# Generated by Django 4.1.1 on 2022-10-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("references", "0011_remove_bookseries_book_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookgenre",
            name="genre_name",
            field=models.CharField(max_length=30, verbose_name="Genre"),
        ),
        migrations.AlterField(
            model_name="bookpublishinghouse",
            name="house_name",
            field=models.CharField(max_length=30, verbose_name="Publishing house"),
        ),
        migrations.AlterField(
            model_name="bookseries",
            name="book_series",
            field=models.CharField(max_length=30, verbose_name="Books in series"),
        ),
    ]
