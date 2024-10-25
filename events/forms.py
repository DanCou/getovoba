from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'players', 'date', 'start_time', 'end_time', 'city', 'location', 'image', 'mode', 'slug']  # Specify the fields to include in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        
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
        self.fields['mode'].required = True  # example of optional
        self.fields['slug'].required = False  # example of optional
