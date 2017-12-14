from django.db import models
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Link(models.Model):
    link = models.URLField()
    hits = models.IntegerField(default=0)
    short_url = models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return self.short_url
