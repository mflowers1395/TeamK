from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User
from users.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User(firstname=form.cleaned_data['firstname'],lastname=form.cleaned_data['lastname'],email=form.cleaned_data['email'],username=form.cleaned_data['username'],CWID=form.cleaned_data['CWID'])
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')  # edit redirect to somewhere else if necessary
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def userAcct(request):
    
    return render(request, 'users/home.html')


    


