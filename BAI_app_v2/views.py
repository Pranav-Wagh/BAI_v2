from django.shortcuts import render
from BAI_app_v2.forms import ParticipantInfoForm,SignUpForm,SpeedForm,SafetynWellfareForm,OthersForm

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
        
        if speed_cat.is_valid():
            speed_cat1 = speed_cat.save()
            speed_cat1.save()

            filled = True

        else:
            print("Chuklay ikde!")
            print(speed_cat.errors)

    else:
        speed_cat = SpeedForm()
        
    return render(request,'BAI_app_v2/form1.html',{'speed_cat':speed_cat,
                                                    'filled':filled})


def form2(request):
    filled2 = False
    if request.method == 'POST':

        safety_cat = SafetynWellfareForm(request.POST,request.FILES)
        others_cat = OthersForm(request.POST,request.FILES)

        if safety_cat.is_valid() and others_cat.is_valid():

            safety_cat1 = safety_cat.save(commit=False)

            others_cat1 = others_cat.save(commit=False)

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
            print("Chuklay ikde!")
            print(safety_cat.errors,others_cat.errors)

    else:
        safety_cat = SafetynWellfareForm()
        others_cat = OthersForm()
        
    return render(request,'BAI_app_v2/form2.html',{'safety_cat':safety_cat,
                                                    'others_cat':others_cat,'filled2':filled2})

