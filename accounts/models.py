from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone

#Model
class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def is_expired(self):
        expiration_time = self.created_at + datetime.timedelta(hours=1)  # Jeton valide pendant 1 heure
        return timezone.now() > expiration_time

    def __str__(self):
        return f"Token for {self.user.email}"
    