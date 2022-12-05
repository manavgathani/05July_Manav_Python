from django import forms
from .models import usersignup,mynotes

class userSignupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class notesform(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'