# Generated by Django 4.2 on 2023-10-25 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="windowmaterial",
            name="category",
            field=models.CharField(
                choices=[("wood", "Wood"), ("metal", "Metal"), ("plastic", "Plastic")],
                default=django.utils.timezone.now,
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="windowmaterial",
            name="quantity",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="windowmaterial",
            name="name",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
