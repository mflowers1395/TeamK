import imp
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class WishlistForm(forms.Form):

    username = forms.CharField(max_length=50)
    isbn = forms.CharField(max_length=13)




