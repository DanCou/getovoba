from django import forms
from .models import Player
from utils.utils import normalize_string

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['firstname', 'lastname', 'team']  # Specify the fields to include in the form


    def clean_firstname(self):
        # Clean the 'firstname' field
        return normalize_string(self.cleaned_data.get('firstname'))


    def clean_lastname(self):
        # Clean the 'lastname' field
        return normalize_string(self.cleaned_data.get('lastname'))
        

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].required = True
        self.fields['lastname'].required = True
        self.fields['team'].required = True

    
    
