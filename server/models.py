from django.db import models

# Create your models here.
class search(models.Model):
    search = models.CharField(max_length = 50,default='')
    
