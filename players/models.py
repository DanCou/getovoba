from django.db import models, IntegrityError
from django.db.models import UniqueConstraint
from django.utils.text import slugify
# from events.models import Event
from teams.models import Team
from datetime import datetime

# Create your models here.

class Player(models.Model):
    lastname = models.CharField("Nom", max_length=50, default="Bond")
    firstname = models.CharField("Prénom", max_length=50, default="James")
    sex = models.CharField("Sexe", max_length=2, choices = [ ("M", "Masculin"), ("F", "Féminin")], default="M")
    birthday = models.DateField("Date", unique=True, blank=True, default=datetime.strptime("01/01/1900", "%d/%m/%Y"))
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players', to_field='slug')
    slug = models.SlugField("Slug", unique=True, blank=True, primary_key=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["lastname", "firstname", "birthday"], name="unique_player")
        ]

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.firstname}-{self.lastname}-{self.birthday.strftime('%Y%m%d')}")
        
        try:
            # Attempt to save the object
            super().save(*args, **kwargs)
        except IntegrityError:
            # Handle the case where the unique constraint is violated
            print(f"A player with the slug '{self.slug}' already exists.")
