from django.conf.urls import url
from contact import views

app_name = 'contact'

urlpatterns = [
    url(r'^contact/', views.contact_view, name ='contact'),
]