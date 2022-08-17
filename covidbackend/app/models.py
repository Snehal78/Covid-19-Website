from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=500, blank=True)
    surname = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    phoneno = models.CharField(max_length=500, blank=True)
    district = models.CharField(max_length=500, blank=True)
    pincode = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=500, blank=True)
    adhaarno = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Contact(models.Model):
    name = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    phoneno = models.CharField(max_length=500, blank=True)
    symptoms = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=255, default="[]")

    def __str__(self):
        return f'{self.name} {self.email}'