from django.conf.urls import url
from experience_app import views

app_name = 'experience_app'

urlpatterns = [
    url(r'^experience/', views.experience, name ='experience'),
]