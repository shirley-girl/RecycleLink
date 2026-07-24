from django.db import models
from django.contrib.auth.models import User

# create your models here.

# this model creates 

class WasteRequest(models.Model):
     
     STATUS_CHOICES = (
          ('pending', 'pending'),
          ('assigned', 'assigned'),
          ('paid', 'paid'), 
          ('approved', 'approved'),
          ('collected', 'collected'),
          ('cancelled', 'cancelled'),
    )
     WASTE_TYPES = (
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
        ('organic', 'Organic'),
    )
     
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     waste_type = models.CharField(max_length=40, choices=WASTE_TYPES)
     location = models.CharField(max_length=255)
     contact_phone = models.CharField(max_length=20)
     preferred_pickup_date = models.DateField()
     status = models.CharField(max_length=20, choices= STATUS_CHOICES, default= 'pending')
     created_at = models.DateTimeField(auto_now_add= True)
     description = models.TextField(
        blank=True,
        help_text="Describe the waste you want collected."
     )
     assigned_company = models.ForeignKey(
         'Company', 
         on_delete= models.SET_NULL, 
         null=True,
         blank=True,
         related_name= 'assigned_pickups'
     )
     

     def __str__ (self):
        return f"{self.user.username}- {self.waste_type}({self.status})"
     


class Company(models.Model):
    # Link the company to a User account for login
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=20)

    description = models.TextField(blank=True, null=True)
    

    # Category of waste the company specializes in
    specialization = models.CharField(
        max_length=100,
        choices=[
            ('plastic', 'Plastic Recycling'),
            ('paper', 'Paper & Cardboard'),
            ('metal', 'Metal Scrap'),
            ('glass', 'Glass'),
            ('organic', 'Organic Waste'),
            ('all', 'General Waste'),
        ],
        default='all'
    )
    
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  






