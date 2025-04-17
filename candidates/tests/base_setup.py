from django.contrib.auth import get_user_model
from django.test import TestCase

from candidates.models import Application
from employers.models import Company, Vacancy


class BaseTestCase(TestCase):
    def setUp(self):
        self.candidate = get_user_model().objects.create_user(
            username="testuser",
            first_name="Test",
            last_name="User",
            password="password123"
        )
        self.company = Company.objects.create(
            name="TestCompany",
            description="TestCompany",
            owner=self.candidate
        )
        self.vacancy = Vacancy.objects.create(
            title="Test Vacancy",
            description="Job description",
            company=self.company,
        )
        self.application = Application.objects.create(
            candidate=self.candidate,
            vacancy=self.vacancy,
            status="pending"
        )
