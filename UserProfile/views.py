from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def launchUserProfile(request):
    return render(request, 'userProfile.html')

def launchSignUpPage(request):
    return render(request, 'register.html')
