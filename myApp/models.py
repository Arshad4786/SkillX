from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Talent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    description = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/')
    approved = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class HireRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    date_sent = models.DateTimeField(auto_now_add=True)  # Only this field needed

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Allow null temporarily
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'Hire Request from {self.client.name} to {self.talent.name}'
