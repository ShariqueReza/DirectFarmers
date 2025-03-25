from django.db import models

# Create your models here.
class contact_us(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return (self.name + ' - ' + self.subject)
    
    
class Area(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True)
    contact_number_1=models.IntegerField(max_length=15,null=True,blank=True)
    contact_number_2=models.IntegerField(max_length=15,null=True,blank=True)
    
    