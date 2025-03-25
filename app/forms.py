from django import forms
from app.models import contact_us

class Contact_UsForm(forms.ModelForm):
    class Meta:
        model=contact_us
        fields={'name','email','subject','message'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Name','style': 'height: 55px;'}),
            'email':forms.EmailInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Email','style': 'height: 55px;'}),
            'subject':forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Subject','style': 'height: 55px;'}),
            'message':forms.TextInput(attrs={'class':'form-control bg-light border-0 px-4','placeholder':'Enter your Message','style': 'height: 55px;'}),
            
        }