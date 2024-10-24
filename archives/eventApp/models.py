from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField("Date")
    event_start_time = models.TimeField("Start Time")
    event_end_time = models.TimeField("End Time")
    event_location = models.CharField("Address", max_length=200)
    event_description = models.CharField("Description", max_length=200, null=True, blank=True)
    event_image = models.ImageField("Image", upload_to='images/', null=True, blank=True)
    event_outdoor = models.BooleanField("Outdoor", default=False)

    def __str__(self):
        return self.event_name + " - " + str(self.event_date.year)
    
class Team(models.Model):
    event = models.ForeignKey(Event, related_name='teams', on_delete=models.CASCADE)
    name = models.CharField("Team Name", max_length=255)

    def __str__(self):
        return self.name

class Player(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255)
    sex = models.CharField("Sex", max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField("Date Of Birth", null=True, blank=True)
    phone_number = models.CharField("Phone Number", max_length=15, null=True, blank=True)
    club_name = models.CharField("Club Name", max_length=255)
    club_zipcode = models.IntegerField(
        "ZipCode",
        # max_length=5,  # Database constraint for maximum length
        # validators=[MinLengthValidator(5), MaxLengthValidator(5)]  # Validation for exact length
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.team.name}"

