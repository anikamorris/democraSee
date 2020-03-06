from django.test import TestCase
from candidates.models import Candidate

class CandidateTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_candidate_slugify_on_save(self):
        candidate = Candidate(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000"
        )
        candidate.save()

        self.assertEqual(candidate.slug, "bernie-sanders")

class CandidateListViewTests(TestCase):
    def test_multiple_candidates(self):
        # Make some test data to be displayed on the page.

        Candidate.objects.create(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000")
    
        Candidate.objects.create(name="Elizabeth Warren", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000")

        # Issue a GET request to homepage.
        response = self.client.get('/candidates/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of candidates passed to the template
        # matches the number of candidates we have in the database.
        responses = response.context['candidates']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Candidate: Bernie Sanders>', '<Candidate: Elizabeth Warren>'],
            ordered=False
        )