from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

# Movie search form
class MovieSearchForm(forms.Form):
    title = forms.CharField(label='Movie Title', max_length=100)

# Registration form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # User class which takes username, email, and password
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Log-in form
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)