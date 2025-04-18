from django.urls import reverse
from candidates.tests.base_setup import BaseTestCase


class CandidateViewsTestCase(BaseTestCase):
    def test_index_view(self):
        response = self.client.get(reverse("candidates:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("vacancies_count", response.context)
        self.assertIn("companies_count", response.context)
        self.assertIn("candidates_count", response.context)

    def test_about_view(self):
        response = self.client.get(reverse("candidates:about"))
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("candidates:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("applications", response.context)
        self.assertIn("vacancies_count", response.context)

    def test_apply_view(self):
        self.assertIn(self.vacancy, self.candidate.vacancies.all())

    def test_toggle_save_vacancy_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse(
            "candidates:toggle_save_vacancy",
            args=[self.vacancy.id])
        )
        self.assertRedirects(response, reverse(
            "employers:vacancies_detail",
            args=[self.vacancy.id])
                             )
        self.assertIn(self.vacancy, self.candidate.saved_vacancies.all())

    def test_saved_vacancies_view(self):
        self.client.login(username="testuser", password="password123")
        self.candidate.saved_vacancies.add(self.vacancy)
        response = self.client.get(reverse("candidates:saved_vacancies"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("vacancies", response.context)
        self.assertIn("is_paginated", response.context)

    def test_applications_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("candidates:applications"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("applications", response.context)
        self.assertEqual(response.context["applications"].paginator.count, 1)
        application = response.context["applications"][0]
        self.assertEqual(application.vacancy.title, "Test Vacancy")
        self.assertEqual(application.status, "pending")
