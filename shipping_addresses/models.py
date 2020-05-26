from django.db import models
from main.models import UserModel

class ShippingAddress(models.Model):
    user = models.ForeignKey(UserModel, related_name="addresses", on_delete=models.CASCADE)
    street = models.CharField(max_length=140)
    external_number = models.PositiveIntegerField()
    internal_number = models.CharField(max_length=10, blank=True, null=True)
    colony = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    references = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.street}, {self.zip_code} ({self.user.full_name})'