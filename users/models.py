from django.db import models
from django.contrib.auth.models import User
import random


class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="confirmation")
    confirmation_code = models.CharField(max_length=6)

    def generate_confirmation_code(self):
        self.confirmation_code = ''.join(random.choices('0123456789', k=6))
        self.save()
        print(self.confirmation_code)

    
    def __str__(self) -> str:
        return self.confirmation_code
