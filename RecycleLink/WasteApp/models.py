from django.db import models

# Create your models here.
"""WasteType_CHOICES = [
    ('Plastic', 'Plastic'),
    ('Paper', 'Paper'),
    ('E-waste', 'E-waste'),
    ('Organic', 'Organic'),
    ('Metal', 'Metal'),
    ('Glass', 'Glass'),
]

class WasteItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=50, choices=WasteType_CHOICES)
    quantity_kg = models.FloatField()
    collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.waste_type} - {self.quantity_kg} kg"
"""

