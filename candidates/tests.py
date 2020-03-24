from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from candidates.models import Candidate, AddedCandidate
from candidates.views import CandidateDetailView, MyCandidatesListView

class CandidateTests(TestCase):
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
        candidate = Candidate(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000"
        )
        candidate2 = Candidate(name="Joe Biden", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000"
        )
        candidate.save()
        candidate2.save()

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
            ['<Candidate: Bernie Sanders>', '<Candidate: Joe Biden>'],
            ordered=False
        )

    def test_slug_goes_to_detail_page(self):
        # Make some test data to be displayed on the page.
        candidate = Candidate(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000"
        )
        candidate.save()

        # Issue a GET request to homepage.
        response = self.client.get('/candidates/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Get candidate's slug
        slug = candidate.slug

        # Issue a GET request to detail page.
        next_response = self.client.get(f'/candidates/{slug}')

        # Check that the response is 200 OK.
        self.assertEqual(next_response.status_code, 200)


class CandidateDetailViewTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'anika',
            'password': 'Anika@12345'}
        self.user = User.objects.create_user(**self.credentials)

    def tearDown(self):
        # Clean up after each test.
        self.user.delete()

    def test_add_candidate(self):
        # Make some test data to be displayed on the page.
        candidate = Candidate(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000"
        )
        candidate.save()
        
        # Attempt to add candidate.
        request = RequestFactory().post(f'/candidates/add-candidate/{candidate.slug}')
        
        # Simulate a logged in user.
        request.user = self.user

        # Render the detail view with the request. 
        response = CandidateDetailView.as_view()(request, candidate.slug)

        # Check that response is 302 "found" redirect.
        self.assertEqual(response.status_code, 302)

        # Check that the user has been redirected to My Candidates page.
        self.assertEqual(response.url, '/candidates/my-candidates/')


class MyCandidatesListViewTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'anika',
            'password': 'Anika@12345'}
        self.user = User.objects.create_user(**self.credentials)
        self.client.login(username='anika', password='Anika@12345')

    def tearDown(self):
        # Clean up after each test.
        self.user.delete()

    def test_add_candidate(self):
        # Make some test data to be displayed on the page.
        candidate = Candidate(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000"
        )
        candidate.save()
        
        # Attempt to add candidate.
        request = self.client.post(f'/candidates/add-candidate/{candidate.slug}')

        # Use the redirected url to render MyCandidatesListView.
        response = self.client.get(request.url)

        # Check that the candidate and user were saved with the AddedCandidate model
        responses = response.context['candidates']
        self.assertQuerysetEqual(
            responses,
            ['<AddedCandidate: anika > Bernie Sanders>',],
            ordered=False
        )