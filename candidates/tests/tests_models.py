from candidates.models import Candidate
from candidates.tests.base_setup import BaseTestCase


class CandidatesModelsTestCase(BaseTestCase):
    def test_candidate_str_method(self):
        self.assertEqual(str(self.candidate), "testuser (Test User)")

    def test_default_role_is_candidate(self):
        self.assertEqual(self.candidate.current_role, Candidate.UserRoles.CANDIDATE)

    def test_vacancies_association(self):
        self.candidate.vacancies.add(self.vacancy)
        self.assertIn(self.vacancy, self.candidate.vacancies.all())

    def test_saved_vacancies_association(self):
        self.candidate.saved_vacancies.add(self.vacancy)
        self.assertIn(self.vacancy, self.candidate.saved_vacancies.all())
