import imp
from turtle import title
from django.shortcuts import render
from Catalogue.models import Textbook

def catalogueInterface(request):
    
    return render(request, 'catalogue/interface.html')

def browseTextbooks(request):

    textbook_list = Textbook.objects.all()

    return render(request, 'catalogue/browse.html', {'textbook_list': textbook_list})

def searchCatalogue(request):

    if request.method == 'POST':

        searchresults = request.POST['searchresults']
        textbook = Textbook.objects.all().filter(booktitle__contains=searchresults) | Textbook.objects.all().filter(author__contains=searchresults) | Textbook.objects.all().filter(isbn__contains=searchresults)
        
        return render(request, 'catalogue/search.html', {'searchresults': textbook})
  
def deleteuploadtext(request):
    t_name= request.POST['textbook']
    return render(request, 'catalogue/delete.html/', {'textbook':t_name})