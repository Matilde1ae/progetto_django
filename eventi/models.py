from django.db import models
from django.conf import settings
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, default="Location Principale")
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organized_events',
    )

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registrations',
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event_participants',
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} partecipa a {self.event.title}"