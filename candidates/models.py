from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Candidate(models.Model):
    name = models.CharField(max_length=100, default="")
    accomplishments = models.TextField(null=True)
    platform = models.TextField(null=True)
    foreign_policy = models.TextField(null=True)
    unique = models.TextField(verbose_name="what sets this candidate apart", null=True)
    total_contributions = models.IntegerField(verbose_name="total independent contributions", default=0)
    is_active = models.BooleanField(verbose_name="is this candidate still in the race", default=True)
    candidate_id = models.CharField(max_length=100, default="")
    slug = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/candidate-name). """
        path_components = {'slug': self.slug}
        return reverse('wiki-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(Candidate, self).save(*args, **kwargs)
