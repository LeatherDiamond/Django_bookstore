# Generated by Django 4.1.1 on 2022-11-20 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product_card", "0011_book_description"),
        ("carts", "0004_alter_booksincart_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booksincart",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="product_card.book",
                verbose_name="Book",
            ),
        ),
    ]
