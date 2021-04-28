from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=200, widget=forms.PasswordInput())
    field_order=['username', 'password', 'password_confirm', 'first_name', 'last_name','email']

    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput}
        fields = ['username', 'password']