# Generated by Django 4.2.5 on 2023-10-18 03:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=1.0, max_digits=10, null=True
            ),
        ),
    ]