from django import forms
from .models import movietable

class movieform(forms.ModelForm):
    class Meta:
        model=movietable
        fields=['name','desc','year','img']

