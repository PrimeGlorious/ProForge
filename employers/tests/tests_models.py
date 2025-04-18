from employers.tests.base_setup import BaseTestCase


class EmployersModelsTestCase(BaseTestCase):
    def test_company_str_method(self):
        self.assertEqual(str(self.company), "Test Company")

    def test_vacancy_str_method(self):
        self.assertEqual(str(self.vacancy), "Test Vacancy")
