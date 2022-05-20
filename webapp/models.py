from django.db import models

# Create your models here.

class Subscrib(models.Model):
    email = models.CharField(max_length=70, default="")

    def __str__(self):
        return self.email

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=70, default="")
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.first_name
