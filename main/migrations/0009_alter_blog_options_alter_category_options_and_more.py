# Generated by Django 4.2.7 on 2023-11-29 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0008_thread_rm_counter"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "ordering": ("-created",),
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs : %(count)s",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="blog",
            name="allow_comments",
            field=models.CharField(
                choices=[("allow", "allow"), ("disallowed", "disallowed")],
                default="disallow",
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("published", "published"), ("draft", "draft")],
                default="draft",
                max_length=30,
            ),
        ),
    ]
