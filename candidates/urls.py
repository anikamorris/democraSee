from django.urls import path

from candidates.views import CandidateListView, CandidateDetailView, MyCandidatesListView

urlpatterns = [
    path('', CandidateListView.as_view(), name='candidate-list-page'),
    path('<str:slug>', CandidateDetailView.as_view(), name='candidate-detail-page'),
    path('my-candidates/', MyCandidatesListView.as_view(), name='my-candidates-list-page')
]