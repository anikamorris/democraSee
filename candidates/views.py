from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from candidates.models import Candidate


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
        data = request.get(f"https://api.open.fec.gov/v1/candidates?api_key=65AZmfF2NYsVgkfOfWN6gWVHTMbFqhZyBjYUUzEc&{candidate.candidate_id}")
        return render(request, 'detail.html', {
            'candidate': candidate
        })