from django import forms
from .models import Event

from utils.utils import normalize_string

import pandas as pd

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'players', 'date', 'start_time', 'end_time', 'city', 'location', 'image', 'mode', 'file']  # Specify the fields to include in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    # def clean_name(self):
    #     # Clean the 'firstname' field
    #     return normalize_string(self.cleaned_data.get('firstname'))
    
    def clean_city(self):
        # Clean the 'city' field
        return normalize_string(self.cleaned_data.get('city'))

        
    def clean_location(self):
        # Clean the 'location' field
        return normalize_string(self.cleaned_data.get('location'))

        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['players'].required = True
        self.fields['date'].required = True
        self.fields['start_time'].required = True
        self.fields['end_time'].required = True
        self.fields['city'].required = True
        self.fields['location'].required = False  # example of optional
        self.fields['image'].required = False  # example of optional
        self.fields['mode'].required = True  
        self.fields['file'].required = False 

    
    
