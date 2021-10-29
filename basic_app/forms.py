from django import forms
from basic_app.models import Subscribers

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'


