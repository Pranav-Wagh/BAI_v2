from django.db import models
from django.contrib.auth.models import User

# Create your models here.
yes_no=[("on","on"),("off","off")]

class ParticipantInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    ph_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    other_membership = models.TextField(blank=True)
    company_nm = models.CharField(max_length=50)
    applicant_desig = models.CharField(max_length=25)

    #applicant_img = models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.user.username

class Speed(models.Model):

    tender = models.CharField(choices=yes_no,max_length=4,blank=False)
    ProTimeFrame = models.TextField(max_length=100,blank=True)

    tracked = models.CharField(choices=yes_no,max_length=4,blank=False)
    PMCappointed = models.CharField(choices=yes_no,max_length=4,blank=False)
    TimeReduc = models.CharField(choices=yes_no,max_length=4,blank=False)
    trackPro = models.CharField(choices=yes_no,max_length=4,blank=False)

    expectPeriod = models.TextField(max_length=100,blank=False)
    periodComplete = models.TextField(max_length=100,blank=False)
    
    difficulty = models.CharField(choices=yes_no,max_length=4,blank=False)
    timeLost = models.TextField(max_length=100,blank=True)

    mechanization = models.TextField(max_length=100,blank=True)
    contribImprov = models.TextField(max_length=100,blank=True)
    tenderPay = models.CharField(choices=yes_no,max_length=4,blank=False)
    suggest = models.TextField(max_length=100,blank=False)
    SpeedScale = models.TextField(max_length=100,blank=False)

    def __str__(self):
        return self.tender

class SafetynWellfare(models.Model):
    monitered = models.CharField(choices=yes_no,max_length=4,blank=False)
    bywhom = models.TextField(max_length=200,blank=False)
    measures =models.TextField(max_length=2000,blank=True)
    medical_aid = models.CharField(choices=yes_no,max_length=4,blank=False)
    incidents = models.CharField(choices=yes_no,max_length=4,blank=False)
    safety_audits = models.FileField(upload_to='uploads',blank=True)

    def __str__(self):
        return self.bywhom

class Others(models.Model):
    accomodation= models.ImageField(upload_to='uploads',blank=False)#
    sanitary = models.ImageField(upload_to='uploads', blank=False)#
    school = models.ImageField(upload_to='uploads', blank=True)
    polution_measures = models.ImageField(upload_to='uploads', blank=False)#
    ISO_accreditation = models.CharField(choices=yes_no,max_length=4,blank=True)
    conseravation_A = models.TextField(max_length=200,blank=False)
    conseravation_B = models.TextField(max_length=200,blank=False)
    renewable_energy_text = models.TextField(max_length=200,blank=True)
    renewable_energy_pic = models.FileField(upload_to='uploads', blank=True)
    green_building = models.TextField(max_length=2000,blank=True)
    debris_management = models.TextField(max_length=2000, blank=True)
    seminars = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.conseravation_A
