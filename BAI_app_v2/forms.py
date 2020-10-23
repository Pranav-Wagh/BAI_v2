from django import forms
from django.contrib.auth.models import User
from BAI_app_v2.models import ParticipantInfo

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class ParticipantInfoForm(forms.ModelForm):
    class Meta():
        model = ParticipantInfo
        fields = ('ph_no','address','other_membership','company_nm','applicant_desig')
