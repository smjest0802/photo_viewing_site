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

    if request.method == 'POST':
        form = LoginForm(request.POST)

        print "here"
        if form.is_valid():
            # Need to validate the login credentials, but for now just go the page
            print "here 2"
            return render(request, 'photo/index.html')
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form':form.as_ul()})

