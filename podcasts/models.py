from django.db import models
from multiselectfield import MultiSelectField
# from pycountry import languages, countries
from uuid import uuid4

# LANGUAGE_CHOICES=
# COUNTRY_CHOICES=

class Podcast(models.Model):

    EPISODIC = "ep"
    SERIAL = "se"
    ITUNES_TYPE_CHOICES = (
        (EPISODIC, "Episodic"),
        (SERIAL, "Serial"),
    )

    title = models.CharField(max_length=20)
    slug = models.SlugField()
    description = models.TextField()
    # language = models.CharField(choices=LANGUAGE_CHOICES)
    #itunes_author
    #itunes_image
    itunes_explicit = models.BooleanField()
    itunes_category = models.CharField(max_length=20)#fix (also feed)
    # itunes_subcategories
    itunes_complete = models.BooleanField(default=False)
    itunes_type = models.CharField(choices=ITUNES_TYPE_CHOICES, max_length=8, default=EPISODIC)
    spotify_limit = models.PositiveSmallIntegerField(blank=True, null=True)
    # spotify_country = models.CharField(choices=COUNTRY_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def description_snippet(self):
        desc = self.description
        if len(desc) > 50:
            return desc[:50] + "..."
        return desc

