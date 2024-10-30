from django.db import models
from django.utils.text import slugify
# from events.models import Event
# from teams.models import Team

# Create your models here.

class Player(models.Model):
    lastname = models.CharField("Nom", max_length=50)
    firstname = models.CharField("Prénom", max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    slug = models.SlugField("Slug", unique=True, blank=True)

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.firstname}-{self.lastname}")
        super().save(*args, **kwargs)
