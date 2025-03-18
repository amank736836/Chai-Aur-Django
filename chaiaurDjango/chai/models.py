from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVarity, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField()
    comment = models.TextField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name} with rating {self.rating}"


class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name="stores")

    def __str__(self):
        return self.name


class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVarity, on_delete=models.CASCADE, related_name="certificate"
    )
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Cerificate for {self.chai.name} with number {self.certificate_number} valid until {self.valid_until}"
