from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_image = models.ImageField(upload_to="event")
    event_view_count = models.PositiveIntegerField(default=1)

class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    attendee_event = models.CharField(max_length=100)


