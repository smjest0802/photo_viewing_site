"""
.. module:: search/views.py
    :platform: Unix
    :synopsis: Generates the views for the search application

.. moduleauthor:: Shawn Meginley <shawn.meginley@gmail.com>
"""

from django.shortcuts import render

from .forms import LoginForm

def LoginView(request):
    """Handles the view for the landing page and login prompt"""

    form = LoginForm()

    return render(request, 'login/login.html', {'form':form.as_ul()})

