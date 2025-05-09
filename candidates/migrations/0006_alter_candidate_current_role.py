# Generated by Django 5.2 on 2025-04-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "candidates",
            "0005_remove_vacancy_company_alter_application_vacancy_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="current_role",
            field=models.CharField(
                choices=[("candidate", "Candidate"), ("employer", "Employer")],
                default="candidate",
                max_length=15,
            ),
        ),
    ]
