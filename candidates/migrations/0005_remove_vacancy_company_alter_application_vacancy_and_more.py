# Generated by Django 5.2 on 2025-04-13 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0004_candidate_current_role"),
        ("employers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vacancy",
            name="company",
        ),
        migrations.AlterField(
            model_name="application",
            name="vacancy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="employers.vacancy",
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="saved_vacancies",
            field=models.ManyToManyField(
                blank=True, related_name="saved_by", to="employers.vacancy"
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="vacancies",
            field=models.ManyToManyField(
                blank=True,
                related_name="candidates",
                through="candidates.Application",
                to="employers.vacancy",
            ),
        ),
        migrations.DeleteModel(
            name="Company",
        ),
        migrations.DeleteModel(
            name="Vacancy",
        ),
    ]
