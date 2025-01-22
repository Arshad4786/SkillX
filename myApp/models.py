from django.db import models
from django.contrib.auth.models import User

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
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Reference Client model
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)  # Reference Talent model
    message = models.TextField()  # The message the client sends
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)  # The timestamp when the request is created

    def __str__(self):
        return f"Hire Request from {self.client.name} for {self.talent.name}"
