# users/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import settings

from .forms import CustomForm

# Create your views here.
def usercreate(request):
    '''Create users form'''
    if request.method != 'POST':
        form = CustomForm()
    else:
        # Post method
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()

            # Log user and and redirect
            #return HttpResponseRedirect(reverse(settings.LOGIN_REDIRECT_URL))

            # Here wouldbe a good place to log the user in and then redirect.
            # Q?: Could you call LOGIN_REDIRECT_URL??
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'createuser.html', {'form': form})
