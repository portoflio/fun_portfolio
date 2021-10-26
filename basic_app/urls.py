from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^profile-amr/$', views.profile, name='amr'),
    url(r'^profile-duygu/$', views.profile, name='duygu'),
    url(r'^profile-harrison/$', views.profile, name='harrison'),
    url(r'^profile-pierre/$', views.profile, name='pierre'),
    url(r'^profile-robert/$', views.profile, name='robert'),
]