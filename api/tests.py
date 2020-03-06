from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from candidates.models import Candidate
from api.serializers import CandidateSerializer

class CandidateListAPITestCase(APITestCase):
    def setUp(self):
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

        Candidate.objects.create(name="Joe Biden", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0002")

    def test_get_all_candidates(self):
        response = self.client.get(reverse('candidates_list'))
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CandidateDetailAPITestCase(APITestCase):
    def setUp(self):
        self.bernie = Candidate.objects.create(name="Bernie Sanders", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000")

        self.warren = Candidate.objects.create(name="Elizabeth Warren", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0000")

        self.biden = Candidate.objects.create(name="Joe Biden", 
            accomplishments="Test",
            platform="Test",
            foreign_policy="Test",
            unique="Test",
            candidate_id="P0002")

    def test_get_valid_single_candidate(self):
        response = self.client.get(reverse('candidates_detail'), kwargs={'pk': self.bernie.pk})
        candidate = Candidate.objects.get(pk=self.bernie.pk)
        serializer = CandidateSerializer(candidate)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
