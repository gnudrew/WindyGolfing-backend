# Generated by Django 4.1.3 on 2022-12-04 23:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("winds", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="windspacetime",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
