'''

INF601 - Programming in Python

Assignment #3:  Mini Project 4

I,     Jose Saumat   , affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism,
or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have
accurately cited all sources in adherence to academic standards. I understand that failing to comply with this
integrity statement may result in consequences, including disciplinary actions as determined by my course instructor
and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles
of academic integrity.

'''

#These classes are used to generate forms and handle user input

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