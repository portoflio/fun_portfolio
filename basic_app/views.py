from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'index.html')


def experience(request):
    return render(request, 'experience.html')
