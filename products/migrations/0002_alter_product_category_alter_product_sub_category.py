# Generated by Django 4.1.5 on 2023-01-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_subcategory"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                related_name="categories", to="categories.category"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="sub_category",
            field=models.ManyToManyField(
                related_name="subcategories", to="categories.subcategory"
            ),
        ),
    ]
