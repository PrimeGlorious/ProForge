from django.urls import reverse

from employers.models import Vacancy
from employers.tests.base_setup import BaseTestCase


class EmployersViewsTestCase(BaseTestCase):

    def test_company_detail_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("employers:company_detail", kwargs={"pk": self.company.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Company")
        self.assertContains(response, "This is a test company description.")

    def test_vacancies_list_view(self):
        response = self.client.get(reverse("employers:vacancies_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Vacancy")

    def test_vacancies_create_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("employers:vacancies_create"))
        self.assertEqual(response.status_code, 200)

    def test_vacancies_manage_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("employers:vacancies_manage"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Vacancy")

    def test_vacancies_delete_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse("employers:vacancies_delete", kwargs={"pk": self.vacancy.pk}))
        self.assertRedirects(response, reverse("employers:vacancies_manage"))
        self.assertEqual(Vacancy.objects.count(), 0)

    def test_vacancies_update_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("employers:vacancies_update", kwargs={"pk": self.vacancy.pk}))
        self.assertEqual(response.status_code, 200)
