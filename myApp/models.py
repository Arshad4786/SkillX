from django.db import models

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
