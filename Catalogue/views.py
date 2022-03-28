import imp
from turtle import title
from django.shortcuts import render, redirect
from django.contrib import messages
from Catalogue.models import Textbook
from User_Registration.models import WishList
from User_Registration.forms import WishlistForm
from django.contrib.auth import get_user_model

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

def wishlistForm(request):

    if request.method == 'POST':

         form = WishlistForm(request.POST)

         if form.is_valid():

             cd = form.cleaned_data

             try:
                 get_user_model().objects.get(username=cd['username'])

                 if WishList.objects.filter(username=cd['username']).exists():

                     wl = WishList.objects.get(username=cd['username'])
                     wl.textbooks.add(Textbook.objects.filter(isbn=cd['isbn']).get())
                     isbn = cd['isbn']
                     messages.success(request, f'Textbook {isbn} added to your wishlist!')
                     return redirect('browse')

                 else:

                     new_wl = WishList.objects.create(username=cd['username'])
                     new_wl.textbooks.add(Textbook.objects.filter(isbn=cd['isbn']))
                     isbn = cd['isbn']
                     messages.success(request, f'Textbook {isbn} added to your wishlist!')
                     return redirect('browse')

             except get_user_model().DoesNotExist:
                 username = cd['username']
                 messages.error(request, f'{username} does not exist')
                 return redirect('browse')

    else:
        messages.error(request, "Invalid request! Textbook was not added to your wishlist")
        return redirect('browse')

    context = {'form': form, 'textbook_list':Textbook.objects.all()}

    return render(request, 'catalogue/wishlistform.html', context)

def deleteuploadtext(request):
    t_name= request.POST['textbook']
    return render(request, 'catalogue/delete.html/', {'textbook':t_name})
