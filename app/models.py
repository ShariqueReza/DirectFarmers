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
    contact_number_1=models.IntegerField(null=True,blank=True)
    contact_number_2=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Veg', 'Vegetable'),
        ('Fruit', 'Fruit'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    areas = models.ManyToManyField(Area, related_name='products')
    
    def __str__(self):
        return self.name
    
    