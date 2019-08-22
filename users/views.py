from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import CustomUserCreationForm

def signup(request):
    if request.method != 'POST':
        # display blank form.
        form = CustomUserCreationForm()
    else:
        # validate data and send the user to login page.
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Q?: What does this actually check for? For example, duplicated
            # usernames??
            # If you try to create someone that already exists it will not work
            # is_valid() must be working in conjunction with the the UserForm
            # and its specific requirements.
            
            # Save the user in DB
            form.save()
            # redirect to the login page.
            # Eventually create this so that the user is automatically logged
            # in.
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'signup.html', {'form': form})
