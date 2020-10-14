from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('Employed', 'Employed'),
    ('Unemployed', 'Unemployed'),
    ('self-employed', 'self-employed'),
)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=12)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    pincode = models.CharField(max_length=10)
    highest_qualification = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='')


