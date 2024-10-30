from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team']  # Specify the fields to include in the form
        
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['team'].required = True

    
    
