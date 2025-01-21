from django.db import models

class Products(models.Model):
    name=models.TextField(max_length=100,verbose_name="producto")
    description=models.TextField(max_length=300,verbose_name="descripción")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="precio")
    available=models.BooleanField(default=True,verbose_name="disponible")
    picture=models.ImageField(upload_to="pictures",null=True,blank=True,verbose_name="imagen")

    def __str__(self):
        return self.name

# Create your models here.
