from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''Custom form for creating new users.'''
    class Meta:
        model = CustomUser
        fields = ['username'] # pswd by default...
        # Assuming labels are coming from the parent class...

class CustomUserChangeForm(UserChangeForm):
    '''Custom form for changing user data.'''
    class Meta:
        model = CustomUser
        fields = ['username']
