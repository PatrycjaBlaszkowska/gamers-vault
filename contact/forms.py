from django import forms
from .models import ContactQuery


class ContactQueryForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['name', 'email', 'query_type', 'order', 'message']

    def __init__(self, *args, **kwargs):
        """ Add placeholders, set labels, manage autofocus, and make fields required """
        super().__init__(*args, **kwargs)
        
        # Set custom placeholders
        placeholders = {

            'message': 'Write your message here...',
        }
    
        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].label = False  
            self.fields[field].required = True
