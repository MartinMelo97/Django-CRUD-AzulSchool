from django.db import models

GENDER_OPTS = (
    ('male', 'Masculino'),
    ('female', 'Femenimo'),
    ('other', 'Otros')
)

class UserModel (models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(choices=GENDER_OPTS, max_length=20)
    date_birth = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'