from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Blog

class MyUserForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(MyUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class MyLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
	class Meta:
		model = User
		fields = ("username", "password")

class BlogForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),min_length=5 ,required=True)
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),min_length=40 ,required=True)
	class Meta:
		model = Blog
		fields=("title","content")