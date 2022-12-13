# Generated by Django 4.1.3 on 2022-12-13 04:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "simulator",
            "0002_rename_prob_aiming_function_simexperiment_prob_aiming_geometry_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="DesignOfExperiments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("placeholder", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="simtrial",
            name="initial_direction",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.FloatField(),
                default=[1, 0, 0],
                max_length=3,
                size=None,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="simtrial",
            name="initial_speed",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="simtrial",
            name="initial_time",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
