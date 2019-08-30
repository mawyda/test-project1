# blogs/forms.py
from django import forms

from .models import Blog
from pagedown.widgets import PagedownWidget

class BlogForm(forms.ModelForm):
    """Blog form."""
    # Pagedown override
    content = forms.CharField(widget = PagedownWidget())

    class Meta:
        # If nothing is added here, will the form still work?
        model = Blog
        fields = ['title', 'content']
        # Can you ignore the labels?
        labels = {'title': 'Title', 'contents': 'Contents'}
