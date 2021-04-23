from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    x=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold')
    ]
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100,null=True,blank=True)
    photo_book=models.ImageField(upload_to='photo_book',null=True,blank=True)
    photo_author=models.ImageField(upload_to='photo_author',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    retal_price_day=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retal_period=models.IntegerField(null=True,blank=True)
    total_rental=models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=100,choices=x)
    category_book=models.ForeignKey(category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title