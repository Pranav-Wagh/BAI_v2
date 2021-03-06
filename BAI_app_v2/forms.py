from django import forms
from django.contrib.auth.models import User
from BAI_app_v2.models import ParticipantInfo, Speed, SafetynWellfare, Others, Economy, Project_info, Quality

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

class Project_infoForm(forms.ModelForm):
    class Meta():
        model = Project_info
        fields = ('project_name','project_address','site_map','client_name','project_cost','applicant_role',
                'applicant_scope','applicantWork_cost',#'time_limit',
                'commencement_date','sched_completion_date',
                'act_completion_date','proj_cost_tilldate','Architect_name','Structural_Consultant_name',
                'Plumbing_Consultant_name','Fire_Consultant_name','Landscaping_Consultant_name','HVAC_Consultant_name',
                'Electrical_Consultant_name','Interior_Designer_name','Project_Management_Consultant_name',
                'MoEF_Consultant_name','req_docs','green_proj','green_project_details')

class QualityForm(forms.ModelForm):
    class Meta():
        model = Quality
        fields = ('any_system_for_coordinating_of_all_drawings','drawing_coordinating_system','PMC',
                'drawing_specification_assessment','consultant_visit_frequency','Decision_recorded',
                'meeting_instruction_book_minute','quality_standard_tender','name_of_quality_standard_approver',
                'in_house_team_quality_control','external_team_to_control_quality','list_quality_assurance_tests_OnSite',
                'list_quality_assurance_tests_Off_Site','sample_Checklist_followed','sample_test_reports','any_special_training_programs',
                'If_Yes_Provide_details','any_special_training_programs_workers','If_Yes_Provide_details_workers','any_Supervision_from_Client_side','Any_other_system_method_mechanism_adopted',
                'system_method_mechanism_adopted','rate_your_project_in_terms_of_quality')
