from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
