from django.db import models
from django.utils.text import slugify
from events.models import Event

# Create your models here.

class Team(models.Model):
    name = models.CharField("Nom de l'équipe", max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False, related_name='teams', to_field='slug')
    slug = models.SlugField("Slug", unique=True, blank=True, primary_key=True)

    def __str__(self):
        return self.slug
    
    def get_players(self):
        return self.players.all()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}")
        
        super().save(*args, **kwargs)
