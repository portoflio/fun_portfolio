#from django.core.mail import message
from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.email




