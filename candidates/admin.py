from django.contrib import admin

from .models import Candidate, AddedCandidate

admin.site.register(Candidate)
admin.site.register(AddedCandidate)