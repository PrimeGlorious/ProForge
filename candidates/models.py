from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from employers.models import Vacancy


class Candidate(AbstractUser):
    class UserRoles(models.TextChoices):
        CANDIDATE = "C", "Candidate"
        EMPLOYER = "E", "Employer"

    vacancies = models.ManyToManyField(
        to=Vacancy,
        related_name="candidates",
        through="Application",
        blank=True
    )
    saved_vacancies = models.ManyToManyField(
        to=Vacancy,
        related_name="saved_by",
        blank=True
    )
    current_role = models.CharField(
        max_length=15,
        choices=UserRoles.choices,
        default=UserRoles.CANDIDATE,
    )

    def __str__(self):
        return self.username + f" ({self.first_name} {self.last_name})"


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = "applied", "Applied"
        INTERVIEWED = "interviewed", "Interviewed"
        HIRED = "hired", "Hired"
        REJECTED = "rejected", "Rejected"

    candidate = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
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
