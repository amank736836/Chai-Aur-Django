from django.db import models
from django.utils import timezone
# Create your models here.


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "Masala Chai"),
        ("KL", "Kadak Chai"),
        ("CL", "Chai Latte"),
        ("CL", "Green Chai"),
        ("BL", "Black Chai"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chai/images")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
