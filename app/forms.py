from django import forms
from .models import NoteApp

class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteApp
        fields = '__all__'