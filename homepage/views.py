from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm

def launchRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User(firstname=form.cleaned_data['firstname'],lastname=form.cleaned_data['lastname'],email=form.cleaned_data['email'],username=form.cleaned_data['username'],CWID=form.cleaned_data['CWID'])
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # return redirect('') -> something will go here once homepage is established
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def launchHomePage(request):
    return render(request, 'home.html')
