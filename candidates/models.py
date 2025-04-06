from django.db import models

class Vacancy(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(null=True)
    company = models.ForeignKey(
        to="Company",
        on_delete=models.CASCADE,
        related_name="vacancies"
    )
    location = models.CharField(max_length=100, null=True)
    contacts = models.CharField(max_length=100, null=True)
    description = models.TextField()
