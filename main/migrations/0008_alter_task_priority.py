# Generated by Django 5.1.4 on 2024-12-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_task_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("1-low", "low"), ("2-medium", "medium"), ("3-high", "high")],
                default="low",
                max_length=8,
            ),
        ),
    ]