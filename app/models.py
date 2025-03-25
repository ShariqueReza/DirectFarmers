from django.db import models

# Create your models here.
class contact_us(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)
    
    