from django.db import models
from podcasts.models import Podcast


class Episode(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_published = models.DateTimeField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def description_snippet(self):
        desc = self.description
        if len(desc) > 50:
            return desc[:50] + "..."
        return desc
