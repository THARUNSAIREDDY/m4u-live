from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Memories4U.models import ImProfile

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"UserName",
			}),
		}

		
class ImForm(forms.ModelForm):
	class Meta:
		model=ImProfile
		fields="__all__"