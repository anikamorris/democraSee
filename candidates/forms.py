from django import forms
from candidates.models import AddedCandidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = AddedCandidate
        fields = []
