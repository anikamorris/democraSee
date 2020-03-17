import requests

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from candidates.models import Candidate

class IndexView(ListView):
    def get(self, request):
        return render(request, 'index.html')


class CandidateListView(ListView):
    model = Candidate

    def get(self, request):
        candidates = self.get_queryset().all()
        return render(request, 'list.html', {
            'candidates': candidates
        })


class CandidateDetailView(DetailView):
    model = Candidate

    def get(self, request, slug):
        candidate = self.get_queryset().get(slug__iexact=slug)
        response = requests.get(f"https://api.open.fec.gov/v1/candidate/{candidate.candidate_id}/totals?api_key=65AZmfF2NYsVgkfOfWN6gWVHTMbFqhZyBjYUUzEc&cycle=2020")
        if response.status_code == 200:
            data = response.json()["results"][0]
            print(data)
            contributions = data["contributions"]
            individual_contributions = data["individual_contributions"]
            small_donations = data["individual_unitemized_contributions"]
            large_donations = data["individual_itemized_contributions"]
        
        return render(request, 'detail.html', {
            'candidate': candidate,
            'total_contributions': contributions,
            'individual_contributions': individual_contributions,
            'small_donations': small_donations,
            'large_donations': large_donations
        })