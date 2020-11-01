from django.shortcuts import render
from BAI_app_v2.forms import ParticipantInfoForm,SignUpForm,SpeedForm,SafetynWellfareForm,OthersForm,EconomyForm,Project_infoForm,QualityForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'BAI_app_v2/index.html')

@login_required
def participant_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup(request):
    
    registered = False

    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        participant_form = ParticipantInfoForm(data=request.POST)

        if signup_form.is_valid() and participant_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()

            profile = participant_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        
        else:
            print(signup_form.errors,participant_form.errors)

    else:
        signup_form = SignUpForm()
        participant_form = ParticipantInfoForm()

    return render(request,'BAI_app_v2/signup.html',
                            {'signup_form':signup_form,
                             'participant_form':participant_form,
                             'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user123 = authenticate(request,username=username,password=password)

        if user123 is not None:
            login(request,user123)
            return HttpResponse("LOGIN SUCCESSFUL!!")

        else:
            print("Someone tried and failed to login!!")
            print("Email used:{} and password used: {}").format(username,password)
            return HttpResponse("Invalid Login Details!!")
    else:
        return render(request,'BAI_app_v2/login.html',{})


def form1(request):

    filled = False
    if request.method == 'POST':

        speed_cat = SpeedForm(data=request.POST)
        project_info_cat = Project_infoForm(request.POST,request.FILES)
        quality_cat = QualityForm(request.POST,request.FILES)
        
        if speed_cat.is_valid() and project_info_cat.is_valid() and quality_cat.is_valid():
            speed_cat1 = speed_cat.save()
            speed_cat1.save()

            project_info_cat1 = project_info_cat.save(commit=False)
            quality_cat1 = quality_cat.save(commit=False)   

            if 'req_docs' in request.FILES:
                project_info_cat1.req_docs = request.FILES['req_docs']  
            if 'site_map' in request.FILES:
                project_info_cat1.site_map = request.FILES['site_map'] 
            if 'green_project_details' in request.FILES:
                project_info_cat1.green_project_details = request.FILES['green_project_details']  

            if 'meeting_instruction_book_minute' in request.FILES:
                quality_cat1.meeting_instruction_book_minute = request.FILES['meeting_instruction_book_minute']
            if 'sample_Checklist_followed' in request.FILES:
                quality_cat1.sample_Checklist_followed = request.FILES['sample_Checklist_followed']
            if 'sample_test_reports' in request.FILES:
                quality_cat1.sample_test_reports = request.FILES['sample_test_reports']
                   
            project_info_cat1.save()
            quality_cat1.save()

            filled = True


        else:
            print("Chuklay ikde!")
            print(speed_cat.errors,project_info_cat.errors,quality_cat.errors)

    else:
        speed_cat = SpeedForm()
        project_info_cat = Project_infoForm()
        quality_cat = QualityForm()
        
    return render(request,'BAI_app_v2/form1.html',{'speed_cat':speed_cat,
                                                    'project_info_cat':project_info_cat,
                                                    'quality_cat':quality_cat,'filled':filled})


def form2(request):
    filled2 = False
    if request.method == 'POST':

        safety_cat = SafetynWellfareForm(request.POST,request.FILES)
        others_cat = OthersForm(request.POST,request.FILES)
        economy_cat = EconomyForm(request.POST)

        if safety_cat.is_valid() and others_cat.is_valid() and economy_cat.is_valid():

            safety_cat1 = safety_cat.save(commit=False)
            others_cat1 = others_cat.save(commit=False)
            economy_cat.save()

            if 'safety_audits' in request.FILES:
                safety_cat1.safety_audits = request.FILES['safety_audits']

            safety_cat1.save()

            others_cat1.accomodation = request.FILES['accomodation']
            others_cat1.sanitary = request.FILES['sanitary']
            others_cat1.polution_measures = request.FILES['polution_measures']

            if 'school' in request.FILES:
                others_cat1.school = request.FILES['school']

            if 'renewable_energy_pic' in request.FILES:
                others_cat1.renewable_energy_pic = request.FILES['renewable_energy_pic']            

            others_cat1.save()

            filled2 = True

        else:
            print("Chuklay ikde!1")
            print(safety_cat.errors)
            print(others_cat.errors)
            print(economy_cat.errors)
            

    else:
        safety_cat = SafetynWellfareForm()
        others_cat = OthersForm()
        economy_cat = EconomyForm()
        
    return render(request,'BAI_app_v2/form2.html',{'safety_cat':safety_cat,
                                                    'others_cat':others_cat,
                                                    'economy_cat':economy_cat,'filled2':filled2})

