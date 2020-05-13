from django.db import models
from django.urls import reverse

GENDER_OPTS = (
    ('male', 'Masculino'),
    ('female', 'Femenimo'),
    ('other', 'Otros')
)

class UserModel(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(choices=GENDER_OPTS, max_length=20)
    date_birth = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('user:detail', args=[self.id])


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='users/profiles/photos', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name

    @property
    def get_image_url(self):
        return self.profile_image.url