from .models import *
from django import forms


class SignUpForm(forms.Form, forms.ModelForm):
	email = forms.CharField(label='Email')
	password = forms.CharField(widget=forms.PasswordInput())
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	address= forms.CharField(label='Address', required=False)
	city= forms.CharField(label='City',required=False)

	class Meta:
		model = User
		fields =('email', 'password','first_name','last_name','address','city')