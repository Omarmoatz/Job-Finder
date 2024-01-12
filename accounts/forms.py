from django import forms
from .models import Profile,User

from django.contrib.auth.forms import UserCreationForm
from utiles.generate_code import genrate_code

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class ActivationForm(forms.Form):
    code = forms.CharField( max_length=8)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_num','address','image']


