from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(label='',
                               max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'نام کاربری خودرا وارد کنید'}))
    password1 = forms.CharField(label='',
                                max_length=20,
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمزعبور دلخواه خود را وارد کنید'}))
    password2 = forms.CharField(label='',
                                max_length=30,
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'رمزخودرا دوباره وارد کنید'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
