from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('jersey', 'Jersey'),
        ('shorts', 'Shorts'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('training gear', 'Training Gear'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, default='No Brand')

    def __str__(self):
        return f"{self.name} - {self.brand}"