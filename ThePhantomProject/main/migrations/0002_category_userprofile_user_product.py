# Generated by Django 4.2.5 on 2023-10-15 04:53

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(default="generic description", max_length=500),
                ),
                ("image", models.ImageField(upload_to="media")),
                ("slug", models.SlugField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Product",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(default="generic description", max_length=500),
                ),
                ("details", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="media")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "category",
                    models.OneToOneField(
                        default=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Product Profiles",
                "ordering": ["category"],
            },
        ),
    ]