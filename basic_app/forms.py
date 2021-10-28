from django import forms
from django.forms import fields
from .models import Users


class ContactForm(forms.Form):
    class meta:
        model = Users
        fields ='_all_'
    # name = forms.CharField()
    # email = forms.EmailField()
    # message = forms.CharField(widget = forms.Textarea)

    
