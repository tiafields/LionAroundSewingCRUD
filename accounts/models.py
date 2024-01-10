from django.db import models

# Create your models here.
class Product(models.Model):
     
    COLORS = (
           ('Black', 'Black'),
           ('Blue', 'Blue'),
           ('Dark Green', 'Dark Green'),
           ('Galaxy', 'Galaxy'),
           ('Gray', 'Gray'),
           ('Green', 'Green'),
           ('Orange', 'Orange'),
           ('Pink', 'Pink'),
           ('Purple', 'Purple'),
           ('Red', 'Red'),
           ('Rifle Green', 'Rifle Green'),
           ('Yellow', 'Yellow'),
           ('White', 'White'),
             )
    
    SIZES = (
           ('Baby', 'Baby'),
           ('Mini', 'Mini'),
           ('Small', 'Small'),
           ('Medium', 'Medium'),
           ('Large', 'Large'),
           ('Extra Large', 'Extra Large'),
            )
    product_Name = models.CharField(max_length=200, null=True)
    product_Type = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    color = models.CharField(max_length=200, null = True, choices = COLORS)
    size = models.CharField(max_length=200, null = True, choices = SIZES)
    quantity = models.IntegerField(null=True)
     

    def __str__(self):
        return self.product_Name
     