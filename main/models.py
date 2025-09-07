from django.db import models

class Product(models.Model):
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
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField()
    brand = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.brand}"