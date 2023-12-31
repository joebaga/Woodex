# Generated by Django 4.2 on 2023-10-25 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DoorMaterial",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="DoorSize",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("width", models.FloatField()),
                ("height", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="DoorStyle",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="WindowMaterial",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="WindowSize",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("width", models.FloatField()),
                ("height", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="WindowStyle",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Window",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="window_images/")),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.windowmaterial",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.windowsize",
                    ),
                ),
                (
                    "style",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.windowstyle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Door",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="door_images/")),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.doormaterial",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.doorsize",
                    ),
                ),
                (
                    "style",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quotes.doorstyle",
                    ),
                ),
            ],
        ),
    ]
