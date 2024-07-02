# Generated by Django 5.0.1 on 2024-01-11 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_blog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.category",
            ),
        ),
    ]