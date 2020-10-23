from django.shortcuts import render
from BAI_app_v2.forms import ParticipantInfoForm,SignUpForm

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
        email = request.POST.get('email')
        password = request.POST.get('password')

        user123 = authenticate(request,email=email,password=password)

        if user123 is not None:
            login(request,user123)
            return HttpResponse("LOGIN SUCCESSFUL!!")

        else:
            print("Someone tried and failed to login!!")
            print("Email used:{} and password used: {}").format(email,password)
            return HttpResponse("Invalid Login Details!!")
    else:
        return render(request,'BAI_app_v2/login.html',{})


