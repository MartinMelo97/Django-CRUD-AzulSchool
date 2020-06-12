from django.db import models
from django.urls import reverse
from main.models import UserModel

class Group(models.Model):
    users = models.ManyToManyField(UserModel, related_name='groups')
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups:detail', args=[self.id])