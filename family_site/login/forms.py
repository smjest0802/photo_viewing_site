"""
.. module:: search/forms.py
    :platform: Unix
    :synopsis: Specification of the forms for the search application

 .. moduleauthor:: Shawn Meginley <shawn.meginley@gmail.com>


"""
from django import forms

CHOICES=[('gmail','Gmail'),
         ('facebook','Facebook'),
         ('twitter', 'Twitter')]


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100, widget=forms.TextInput(attrs={'class': 'username'}), required=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(attrs={'class': 'password'}), required=True)

    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'which_type'}), label=False, required=True)

