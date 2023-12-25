# Generated by Django 4.2.7 on 2023-12-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0018_category_context"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="banner",
            field=models.ImageField(blank=True, upload_to="category_banners"),
        ),
        migrations.AddField(
            model_name="category",
            name="banner_small",
            field=models.ImageField(blank=True, upload_to="category_banners_small"),
        ),
    ]
