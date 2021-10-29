from django import forms
from basic_app.models import Subscribers

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'


from django.forms import fields
from .models import Users


class ContactForm(forms.Form):
    class meta:
        model = Users
        fields ='_all_'
    
    
