from django import forms
from django.contrib.auth.models import User
from BAI_app_v2.models import ParticipantInfo, Speed, SafetynWellfare, Others, Economy

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class ParticipantInfoForm(forms.ModelForm):
    class Meta():
        model = ParticipantInfo
        fields = ('ph_no','address','other_membership','company_nm','applicant_desig')

class SpeedForm(forms.ModelForm):
    class Meta():
        model = Speed
        fields = ('tender','ProTimeFrame','tracked','PMCappointed','TimeReduc',
                'trackPro','expectPeriod','periodComplete','difficulty','timeLost',
                'mechanization','contribImprov','tenderPay','suggest','SpeedScale')

class SafetynWellfareForm(forms.ModelForm):

    class Meta():
        model = SafetynWellfare
        fields = ('monitered','bywhom','measures','medical_aid',
                'incidents','safety_audits')

class OthersForm(forms.ModelForm):
    class Meta():
        model = Others
        fields = ('accomodation','sanitary','school','polution_measures',
                'ISO_accreditation','conseravation_A','conseravation_B',
                'renewable_energy_text','renewable_energy_pic','green_building',
                'debris_management','seminars')

class EconomyForm(forms.ModelForm):
    class Meta():
        model = Economy
        fields = ('project_cost','who_determined','cost_reduction',
                'tracked_e','who_tracked','PMC_appointed','expected_cost',
                'actual_cost','difficulty_e','escalated','costsaving_measures',
                'suggestions','cost_per_sft','cost_per_room','cost_per_bed',
                'cost_per_workstation','cost_per_similar','economy_ratings')
