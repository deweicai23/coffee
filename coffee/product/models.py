from django.db import models
from account.models import User



class Product(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    sale = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pubDateTime']


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title + '-' + str(self.id)
    
    class Meta:
        ordering = ['-pubDateTime']
        

class Order(models.Model):
    fullName = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    number = models.IntegerField()
    
    
    def __str__(self):
        return self.fullName        
    



