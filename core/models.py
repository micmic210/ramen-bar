from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations"
    )
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("date", "time") # Prevent double bookings
        ordering = ["-date", "-time"]

        def __str__(self):
            return f"Reservation by {self.user} on {self.date} at {self.time}"