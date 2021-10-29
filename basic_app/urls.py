from django.conf.urls import url
from basic_app import views
from django.contrib import admin

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^profile-amr/$', views.profile, name='amr'),
    url(r'^profile-duygu/$', views.profile, name='duygu'),
    url(r'^profile-harrison/$', views.profile, name='harrison'),
    url(r'^profile-pierre/$', views.profile, name='pierre'),
    url(r'^profile-robert/$', views.profile, name='robert'),
    url(r'^profile-robert/$', views.profile, name='robert'),
   
   
    # url(r'^signup/$', views.users, name='signup'),
    url(r'^contact/', views.form1, name="contact"),
    url(r'^admin/',admin.site.urls),
    
]