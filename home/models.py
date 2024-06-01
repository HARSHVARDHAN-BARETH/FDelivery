from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null = True, blank = True)

class Product(models.Model):
    name = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Adjust max_digits as needed
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='media/')
   
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)    

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default="-----", max_length=200, null=True)
    title = models.CharField(default="---------", max_length=200, null=True)
    desc_text = "--------------"
    desc = models.CharField(default=desc_text, max_length=200, null=True)
    profileImg = models.ImageField(default="media/default.jpg",upload_to='media', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username}s Profile'
