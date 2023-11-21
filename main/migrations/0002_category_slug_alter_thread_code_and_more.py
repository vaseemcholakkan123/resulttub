# Generated by Django 4.2.7 on 2023-11-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="thread",
            name="code",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="thread",
            name="related_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AlterField(
            model_name="thread",
            name="tail_text",
            field=models.TextField(blank=True, null=True),
        ),
    ]
