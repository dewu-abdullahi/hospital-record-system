from django.db import models
from accounts.models import CustomUser
from django.conf import settings

# Create your models here.

class MedicalRecord(models.Model):

    GENDER_CHOICE = [
                ('M', 'Male'),
                ('F', 'Female')
                ]
    GENOTYPE = [
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS')
    ]
    patient_name = models.CharField(max_length=255, null=True)
    doctors_name = models.CharField(max_length=255, null=True)
    genotype = models.CharField(max_length=2, choices=GENOTYPE, null=True)
    blood_group = models.CharField(max_length=2, null=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    symptoms = models.TextField(null=True)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   


    def __str__(self):
        return self.diagnosis


