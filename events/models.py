from django.db import models
from django.utils.text import slugify

# Create your models here.

class Event(models.Model):
    name = models.CharField("Nom du tournoi", max_length=200, unique=True, blank=True)
    players = models.IntegerField("Nombre de joueurs par équipe", choices = [ (2, 2), (3, 3), (4, 4), (6, 6) ], default=3)
    date = models.DateField("Date", unique=True, blank=True)
    start_time = models.TimeField("Heure de début", unique=True, blank=True)
    end_time = models.TimeField("Heure de fin", unique=True, blank=True)
    city = models.CharField("Ville", max_length=200, unique=True, blank=True)
    location = models.CharField("Lieu", max_length=200, null=True, blank=True)
    image = models.ImageField("Image", upload_to='events/', null=True, blank=True)
    mode = models.CharField("Indoor/Outdoor", max_length=10, choices = [ ("indoor", "Indoor"), ("outdoor", "Outdoor")], default="indoor")
    file = models.FileField("fichier HelloAsso", upload_to='uploads/', null=True, blank=True)
    slug = models.SlugField("Slug", unique=True, blank=True, primary_key=True)

    def __str__(self):
        return self.name + " - "    + self.city + " - " \
                                    + str(self.date.year) + " - " \
                                    + str(self.players) + "x" + str(self.players) + " - " \
                                    + self.mode
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.date.year}-{self.city}")
        super().save(*args, **kwargs)
