from django import forms
from basic_app import forms
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Users

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form1(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
#if the user requests to send a form, this checks if the form is valid
     
        if form.is_valid():
            print("Validation success")
            
        if request.POST.get('name')and request.POST.get('email') and request.POST.get('message'):
            pst=Users()
                 
            pst.name = request.POST.get('name')
            pst.email = request.POST.get('email')
            pst.message = request.POST.get('message')
            pst.save()
            form = ContactForm()
           
    return render(request, 'contact.html')
        
        
       
            
           
    