from django.urls import path

from candidates.views import CandidateListView, CandidateDetailView

urlpatterns = [
    path('', CandidateListView.as_view(), name='candidate-list-page'),
    path('<str:slug>', CandidateDetailView.as_view(), name='candidate-detail-page'),
]