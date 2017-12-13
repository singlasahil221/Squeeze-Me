from django.db import models

class Link(models.Model):
    link = models.URLField()
    hits = models.IntegerField(default=0)
    short_url = models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return self.short_url