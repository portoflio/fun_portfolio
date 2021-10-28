from django.conf.urls import url
from basic_app import views
from django.contrib import admin

app_name = 'basic_app'

urlpatterns = [
    # url(r'^signup/$', views.users, name='signup'),
    url(r'^contact/', views.form1, name="contact"),
    url(r'^admin/',admin.site.urls),
    
]