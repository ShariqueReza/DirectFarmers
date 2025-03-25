from django import forms
from app.models import contact_us

class Contact_UsForm(forms.ModelForm):
    class Meta:
        model=contact_us
        fields={'name','email','subject','message'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Email'}),
            'subject':forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Subject'}),
            'message':forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Message'}),
            
        }