from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField("date")
    event_location = models.CharField(max_length=200)
    event_description = models.CharField(max_length=200)
    event_image = models.CharField(max_length=200)
    event_start_time = models.DateTimeField("start time")
    event_end_time = models.DateTimeField("end time")

