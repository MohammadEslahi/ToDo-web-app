# Generated by Django 5.1.4 on 2024-12-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_customuser_categories_remove_customuser_tasks"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="profile_image/default_profile_image.jpg",
                null=True,
                upload_to="profile_image/",
            ),
        ),
    ]
