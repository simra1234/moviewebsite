from django import forms

from . models import *

class fmod(forms.ModelForm):
    class Meta:
       model= akbar
       fields="__all__"

