from django.db import models

# Create your models here.
from django.db import models

class SubscribeModel(models.Model):
    email = models.EmailField(null=False, max_length=200, unique=True)

    def __str__(self):
        return self.email

class Subscribers(models.Model):

    email = models.EmailField(unique=True, null=False)
    def __str__(self):
        return self.email