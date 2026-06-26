from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
    ('organizer', 'Organizer'),
    ('attendee', 'Attendee'),
    )
    email = models.EmailField(max_length=254, blank = True, null = True, verbose_name='Indirizzo Email')
    numero_telefono = models.CharField(max_length=10, blank=True, null=True, verbose_name="numero telefono")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee', verbose_name='Ruolo')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"