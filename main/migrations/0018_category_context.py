# Generated by Django 4.2.7 on 2023-12-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_remove_thread_rm_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="context",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]