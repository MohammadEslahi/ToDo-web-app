# Generated by Django 5.1.4 on 2024-12-13 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_task_author_alter_category_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="author",
        ),
        migrations.RemoveField(
            model_name="task",
            name="author",
        ),
    ]
