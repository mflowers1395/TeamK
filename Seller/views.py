from django.shortcuts import render, redirect
from django.contrib import messages
from Seller.forms import UploadTextbookForm
from Catalogue.models import Textbook
from django.contrib.auth.models import User


def sellInterface(request):
    return render(request, 'seller/interface.html')

def uploadText(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = UploadTextbookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tb = Textbook(booktitle = cd['title'], author = cd['author'], isbn = cd['isbn'], poster = request.user)
            tb.save()
            booktitle = cd.get('title')
            messages.success(request, f'{booktitle} successfully uploaded to catalogue!')
            return redirect ('seller')

    else:
        form = UploadTextbookForm()
    return render(request, 'seller/uploadText.html', {'form': form})
