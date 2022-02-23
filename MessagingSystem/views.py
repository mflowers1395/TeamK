from django.shortcuts import render
from django.http import HttpResponse

def launchMessagingPannel(request):
    return render(request, 'messagingPannel.html')