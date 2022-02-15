from cgitb import html
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

students = [
     {
        'first_name': 'Damian',
        'last_name': 'Adams',
        'user_name': 'dadams1',
        'CWID': 'A12345678',
    }, 
    {
        'first_name': 'Kate',
        'last_name': 'Jones',
        'user_name': 'kjones2',
        'CWID': 'A87654321',
    }
]

def home(request):
    context = {
        'students': Students.objects.all(),
        'title': 'User portal'
    }
    return render(request, 'students/students.html', context)
    


