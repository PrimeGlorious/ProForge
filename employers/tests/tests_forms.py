from django.test import TestCase
from employers.models import Company, Vacancy
from django.contrib.auth import get_user_model

from employers.forms import VacancyForm, CompanyForm


class CompanyFormTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password123")
        self.company_data = {
            "name": "Test Company",
            "website": "https://example.com",
            "description": "This is a test company"
        }

    def test_company_form_valid(self):
        self.client.login(username="testuser", password="password123")
        form = CompanyForm(data=self.company_data)
        self.assertTrue(form.is_valid())

    def test_company_form_invalid(self):
        self.client.login(username="testuser", password="password123")
        invalid_data = self.company_data.copy()
        invalid_data["name"] = ""
        form = CompanyForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])

class VacancyFormTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password123")
        self.company = Company.objects.create(name="Test Company", website="https://example.com",
                                              description="This is a test company", owner=self.user)
        self.vacancy_data = {
            "title": "Test Vacancy",
            "company": self.company,
            "description": "Test vacancy description",
            "salary": 1000
        }
        self.vacancy = Vacancy.objects.create(**self.vacancy_data)

    def test_vacancy_form_valid(self):
        self.client.login(username="testuser", password="password123")
        form = VacancyForm(data=self.vacancy_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_vacancy_form_invalid_missing_title(self):
        self.client.login(username="testuser", password="password123")
        invalid_data = self.vacancy_data.copy()
        invalid_data["title"] = ""
        form = VacancyForm(data=invalid_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["title"])

    def test_vacancy_form_invalid_missing_salary(self):
        self.client.login(username="testuser", password="password123")
        invalid_data = self.vacancy_data.copy()
        invalid_data["salary"] = ""
        form = VacancyForm(data=invalid_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("This field cannot be empty.", form.errors["salary"])

    def test_vacancy_form_invalid_salary_not_integer(self):
        self.client.login(username="testuser", password="password123")
        invalid_data = self.vacancy_data.copy()
        invalid_data["salary"] = "not-a-number"
        form = VacancyForm(data=invalid_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn("Enter a whole number.", form.errors["salary"])
