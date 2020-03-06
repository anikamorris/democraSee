from rest_framework.serializers import ModelSerializer

from candidates.models import Candidate

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'name', 
            'accomplishments', 
            'platform', 
            'foreign_policy',
            'unique',
            'is_active',
            'candidate_id',
        ]