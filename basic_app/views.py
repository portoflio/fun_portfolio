
from django.shortcuts import render
from django.contrib import messages
from basic_app.forms import SubscribeForm
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

def profile(request):
    str_req = str(request)    
    if 'amr' in str_req:
        title = 'Amr'
    elif 'duygu' in str_req:
        title = 'Duygu'
    elif 'harrison' in str_req:
        title = 'Harrison'
    elif 'pierre' in str_req:
        title = 'Pierre'
    elif 'robert' in str_req:
        title = 'Robert'
    else:
        title = str_req
    return render(request, 'profile.html', {'title':title})

def services(request):
    return render(request, 'services.html')

def subscribe(request):
    
    form = SubscribeForm()
    print("BANAN!!!!!asdasdasd")
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        print(request.POST)
        print(form)
        print("TOMATO")    
        if form.is_valid():
            print("Email:" + form.cleaned_data['email'])
            form.save(commit=True)
            print("GURKA")
            messages.success(request,"Subscription successfully completed!")
        else:
             print('COFFE')
             messages.success(request,"Invalid email adress!")
    
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
        
        
       
            
           
    
