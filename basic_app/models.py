from django.db import models

# Create your models here.
from django.db import models

class Subscribers(models.Model):

    email = models.EmailField(unique=True, null=False)
    def __str__(self):
        return self.email




