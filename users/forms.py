from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    fname = forms.CharField(max_length=50, required=True)
    lname = forms.CharField(max_length=50, required=True)
    role = forms.ChoiceField(choices=[('user', 'User'), ('admin', 'Admin')], required=True)
    phone = forms.CharField(max_length=11, required=False)
    company_name = forms.CharField(max_length=255, required=False)

    class Meta:
        model = CustomUser
        fields = ("fname", "lname", "email", "role", "phone", "company_name")