from django.shortcuts import render

# Create your views here.
def launchLandingPage(request):
    return render(request, 'landingpage/landing.html')