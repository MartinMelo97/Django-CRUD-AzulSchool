from django import forms
from .models import UserModel, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['profile_image', 'bio', 'is_public']
        exclude = ['user']