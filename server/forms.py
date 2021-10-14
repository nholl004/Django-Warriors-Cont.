from django import forms
from .models import search

class serverForm(forms.ModelForm):
    class Meta:
        model = search
        fields = [
            'search'
        ]