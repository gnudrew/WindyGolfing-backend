# Generated by Django 4.1.3 on 2022-12-04 22:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import winds.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WindGeneratorParameters",
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
                ("is_windless", models.BooleanField()),
                ("is_constant", models.BooleanField()),
                ("is_oscillatory", models.BooleanField()),
                ("is_lorenz", models.BooleanField()),
                (
                    "base_speed",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(),
                        default=winds.models.set_triple_0,
                        max_length=3,
                        size=None,
                    ),
                ),
                (
                    "frequency",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(),
                        default=winds.models.set_triple_0,
                        max_length=3,
                        size=None,
                    ),
                ),
                (
                    "amplitude",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(),
                        default=winds.models.set_triple_0,
                        max_length=3,
                        size=None,
                    ),
                ),
                (
                    "phase_offset",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(),
                        default=winds.models.set_triple_0,
                        max_length=3,
                        size=None,
                    ),
                ),
                ("rho", models.FloatField(default=0, null=True)),
                ("sigma", models.FloatField(default=0, null=True)),
                ("beta", models.FloatField(default=0, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WindSpacetime",
            fields=[
                ("created_at", models.DateTimeField(auto_now=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                (
                    "generator_name",
                    models.CharField(
                        choices=[
                            ("windless", "windless"),
                            ("constant", "constant"),
                            ("oscillatory", "oscillatory"),
                            ("lorenz", "lorenz"),
                        ],
                        max_length=30,
                    ),
                ),
                ("duration", models.FloatField()),
                ("blob_filename", models.CharField(max_length=50, null=True)),
                (
                    "generator_parameters",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="winds.windgeneratorparameters",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
