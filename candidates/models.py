from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField()
    website = models.URLField(null=True)


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


class Candidate(AbstractUser):
    class UserRoles(models.TextChoices):
        CANDIDATE = "C", "Candidate"
        EMPLOYER = "E", "Employer"

    vacancies = models.ManyToManyField(to=Vacancy, related_name="candidates", through="Application", blank=True)
    saved_vacancies = models.ManyToManyField(to=Vacancy, related_name="saved_by", blank=True)
    current_role = models.CharField(
        max_length=15,
        choices=UserRoles.choices,
        default=UserRoles.CANDIDATE,
    )


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = "applied", "Applied"
        INTERVIEWED = "interviewed", "Interviewed"
        HIRED = "hired", "Hired"
        REJECTED = "rejected", "Rejected"

    candidate = models.ForeignKey(
        to=Candidate,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    vacancy = models.ForeignKey(
        to=Vacancy,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default=Status.APPLIED)
