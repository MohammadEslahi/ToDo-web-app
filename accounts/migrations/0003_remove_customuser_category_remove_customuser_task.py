# Generated by Django 5.1.4 on 2024-12-12 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_customuser_category_customuser_task"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="category",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="task",
        ),
    ]