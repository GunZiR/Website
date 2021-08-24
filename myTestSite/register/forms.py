from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'line_id', 'facebook', 'twitter')
    
    
class UpdateForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'line_id', 'facebook', 'twitter')