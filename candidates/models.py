from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Candidate(models.Model):
    name = models.CharField(max_length=100, default="")
    image_link = models.CharField(max_length=500, null=True)
    accomplishments = models.TextField(null=True)
    platform = models.TextField(null=True)
    foreign_policy = models.TextField(null=True)
    unique = models.TextField(verbose_name="what sets this candidate apart", null=True)
    is_active = models.BooleanField(verbose_name="is this candidate still in the race", default=True)
    candidate_id = models.CharField(max_length=100, default="")
    slug = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/candidate-name). """
        path_components = {'slug': self.slug}
        return reverse('candidate-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(Candidate, self).save(*args, **kwargs)


class AddedCandidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__() + " > " + self.candidate.name