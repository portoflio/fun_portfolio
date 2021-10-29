
from django.shortcuts import render
from django.contrib import messages
from basic_app.forms import SubscribeForm

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


def subscribe(request):
    
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        print(request.POST)
        if form.is_valid():
            print("Email:" + form.cleaned_data['email'])
            form.save(commit=True)
            messages.success(request,"Subscription successfully completed!")
        else:
             messages.success(request,"Invalid email adress!")
    
        return render(request, 'index.html')
