from django.shortcuts import render

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