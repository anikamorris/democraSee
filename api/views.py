from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from candidates.models import Candidate
from api.serializers import CandidateSerializer


class CandidateList(ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetail(RetrieveDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer