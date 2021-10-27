from django import forms
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form1(request):
     return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
#if the user requests to send a form, this checks if the form is valid
        if form.is_valid():
            subject = "Send Us a message"
            bodyc= {
            'first_name': forms.cleaned_data['first_name'],
            'last_name':  form.cleaned_data['last_name'],
            'email': form.cleaned_data['email_address'],
            'message': form.cleaned_data['message'],

            }
            #joining all the body's values together to format the actual email
            message = "\n".join(bodyc.values)

            try:
                send_mail(subject, message, 'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found.')
            return redirect("main:homepage")
        form = ContactForm()
        return render(request, "Home/contact.html",{'form':form})

    
    