from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du tournoi")
    players = models.IntegerField("Nombre de joueurs par équipe", choices = [ (2, 2), (3, 3), (4, 4), (6, 6) ], default=3)
    date = models.DateField("Date")
    start_time = models.TimeField("Heure de début")
    end_time = models.TimeField("Heure de fin")
    location = models.CharField("Lieu", max_length=200)
    description = models.CharField("Description", max_length=200, null=True, blank=True)
    image = models.ImageField("Image", upload_to='events/', null=True, blank=True)
    mode = models.CharField("Indoor/Outdoor", max_length=10, choices = [ ("indoor", "Indoor"), ("outdoor", "Outdoor")], default="indoor")

    def __str__(self):
        return self.name + " - " + str(self.date.year) + str(self.players) + "x" + str(self.players) + " - " + self.mode
