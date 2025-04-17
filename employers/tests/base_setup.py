from django.contrib.auth import get_user_model
from django.test import TestCase

from employers.models import Company, Vacancy


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.company = Company.objects.create(
            name="Test Company",
            description="This is a test company description.",
            owner=self.user
        )
        self.vacancy = Vacancy.objects.create(
            title="Test Vacancy",
            company=self.company,
            description="Job description."
        )
