from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICE = [
        ('user', 'User'),     # Regular User
        ('buyer', 'Buyer'),   # Buyer
        ('vendor', 'Vendor')  # Vendor
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    def is_user(self):
        return self.role == 'user'
    
    def is_buyer(self):
        return self.role == 'buyer'
    
    def is_vendor(self):
        return self.role == 'vendor'
