from django.db import models

# Create your models here.

class STATUS(object):
    EMPLOYED = 1
    UNEMPLOYED = 2
    SELF_EMPLOYED = 3

class Contact(models.Model):
    STATUS_CHOICES = (
        (STATUS.EMPLOYED, 'Employed'),
        (STATUS.UNEMPLOYED, 'Unemployed'),
        (STATUS.SELF_EMPLOYED, 'self-employed'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=12)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    pincode = models.CharField(max_length=10)
    highest_qualification = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True, blank=True)


