from cProfile import label
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'username', 'CWID']
        label = {'firstname': "First name", 'lastname': "Last name", 'email': "Email", 'username': "Username", 'CWID': "CWID",}

    def __init__(self, *args, **kwargs):
       super(UserRegisterForm, self).__init__(*args, **kwargs)
       del self.fields['password1']
       del self.fields['password2']