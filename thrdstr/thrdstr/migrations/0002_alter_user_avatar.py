# Generated by Django 4.2 on 2023-04-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thrdstr", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default="avatars/default.jpg", null=True, upload_to="avatars"
            ),
        ),
    ]
