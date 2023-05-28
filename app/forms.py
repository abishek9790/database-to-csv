from django import forms
from app.models import *

class csv_form(forms.ModelForm):
    class Meta:
        model=csvs
        fields='__all__'

