from django.urls import path

from api.views import CandidateList, CandidateDetail

urlpatterns = [
    path('candidates/', CandidateList.as_view(), name='candidates_list'),
    path('candidates/<int:pk>', CandidateDetail.as_view(), name='candidates_detail'),
]