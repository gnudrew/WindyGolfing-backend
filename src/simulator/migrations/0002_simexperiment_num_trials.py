# Generated by Django 4.1.3 on 2022-12-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simulator", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="simexperiment",
            name="num_trials",
            field=models.IntegerField(null=True),
        ),
    ]
