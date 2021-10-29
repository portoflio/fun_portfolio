from django.contrib import admin
from basic_app.models import Subscribers

# Register your models here.
admin.site.register(Subscribers)
from basic_app.models import Users


admin.site.register(Users)

