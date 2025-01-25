# Generated by Django 5.0 on 2025-01-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="destination",
            name="image",
            field=models.ImageField(
                default="images/destination/default.jpg", upload_to="images/"
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="image",
            field=models.ImageField(
                default="images/trip/default.jpg", upload_to="images/"
            ),
        ),
    ]
