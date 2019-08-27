# blogs/forms.py
from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        # If nothing is added here, will the form still work?
        model = Blog
        fields = ['title', 'content']
        # Can you ignore the labels?
        labels = {'title': 'Title', 'contents': 'Contents'}
        
