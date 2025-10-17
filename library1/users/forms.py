from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']
        help_texts={
           'username':' ',
            'password1':' ',
            'password2':' '
        }
from django import forms
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)