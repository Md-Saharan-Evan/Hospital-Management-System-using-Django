# Generated by Django 4.1.7 on 2023-04-15 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0002_testreport"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
            fields=[
                (
                    "prescription_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("prescription_image", models.ImageField(upload_to="prescriptions/")),
                (
                    "doctor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.doctors",
                    ),
                ),
            ],
        ),
    ]