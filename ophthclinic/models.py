from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
# Create your models here.

class User(AbstractUser):
    pass

class info(models.Model):
    datesubmitted = models.DateTimeField(blank=True, null=True)
    leftleft = models.FloatField(blank=True, null=True)
    leftmiddle = models.FloatField(blank=True, null=True)
    leftright = models.FloatField(blank=True, null=True )
    rightleft = models.FloatField(blank=True, null=True)
    rightmiddle = models.FloatField(blank=True, null=True)
    rightright = models.FloatField(blank=True, null=True)
    leftleftr = models.FloatField(blank=True, null=True)
    leftmiddler = models.FloatField(blank=True, null=True)
    leftrightr = models.FloatField(blank=True, null=True )
    rightleftr = models.FloatField(blank=True, null=True)
    rightmiddler = models.FloatField(blank=True, null=True)
    rightrightr = models.FloatField(blank=True, null=True)
    idpdist = models.FloatField(blank=True, null =True)
    idpread = models.FloatField(blank=True, null=True)
    diabetesmellitus = models.BooleanField(default=None)
    deabetesnumber = models.FloatField(blank=True, null=True)
    hypertension = models.BooleanField(default=False)
    ihd = models.BooleanField(default=False)
    cvs = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    atopy = models.BooleanField(default=False)
    liver = models.BooleanField(default=False)
    kidney = models.BooleanField(default=False)
    cataract = models.BooleanField(default=False)
    glucoma = models.BooleanField(default=False)
    glucomasurgery = models.BooleanField(default=False)
    refractive = models.BooleanField(default=False)
    medication = models.CharField(blank=True, null=True,max_length=400)
    bov = models.BooleanField(default=False)
    diplopia = models.BooleanField(default=False)
    headache = models.BooleanField(default=None)
    burning = models.BooleanField(default=False)
    foreign = models.BooleanField(default=False)
    epiphoria = models.BooleanField(default=False)
    glare = models.BooleanField(default=False)
    note = models.CharField(blank=True, null=True,max_length=1000)

class dosageforms(models.Model):
    name = models.CharField(max_length=20)

class medications(models.Model):
    name = models.CharField(max_length=100)
    concentration = models.IntegerField()
    dosage = models.ForeignKey('dosageforms', on_delete=models.CASCADE)

class thewholemed(models.Model):
    drug = models.ForeignKey('medications', on_delete=models.CASCADE)
    start = models.DateField()
    to = models.DateField()
    perday = models.IntegerField()

class prescription(models.Model):
    patientmed =models.ManyToManyField('thewholemed')
    datesubmitted = models.DateTimeField(auto_now=True)


class client(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    yearofbirth = models.IntegerField(blank=True, null=True)
    relatedprofiles = models.ManyToManyField('info', null = True, blank=True, related_name='relatedprofiles')
    lastprofile = models.ForeignKey('info', null=True, blank=True,  on_delete = models.CASCADE, related_name='lastprofile')
    relatedprescriptions = models.ManyToManyField('prescription', null=True, blank = True)
