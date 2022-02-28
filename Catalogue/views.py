import imp
from django.shortcuts import render
from catalogue.models import Textbook

def catalogueInterface(request):
    
    return render(request, 'catalogue/interface.html')

def browseTextbooks(request):

    textbook_list = Textbook.objects.all()

    return render(request, 'catalogue/browse.html', {'textbook_list': textbook_list})
