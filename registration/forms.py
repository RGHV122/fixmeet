from django.forms import ModelForm
from .models import MyUser,MyUserManager
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


TITLE_CHOICES= [
	('NA','Rather not specify'),
    ('doctor', 'Doctor'),
    ('engineer', 'Engineer'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
    ('businessman', 'Businessman'),
    ]

GENDER_CHOICES = [
	('M','Male'),
	('F','Female'),
	('T','Transgender'),
]
class RegistrationForm(UserCreationForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class':'form-control'}))
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs = {'class':'form-control'}))
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs = {'placeholder':'Email','class':'form-control'}))
	title= forms.CharField(label='Title',widget=forms.Select(choices=TITLE_CHOICES ,attrs={'class':'form-control'}))
	gender= forms.CharField(label='Gender',widget=forms.Select(choices=GENDER_CHOICES ,attrs={'class':'form-control'}))
	name = forms.CharField(label='Name', widget=forms.TextInput(attrs = {'class':'form-control'}))
	class Meta:
		model = get_user_model()
		fields = ['email','name','title','gender']
	def clean_password(self):
		pass1 = self.cleaned_data.get('password1')
		pass2 = self.cleaned_data.get('password2')
		if pass1 and pass2 and pass1 != pass2:
			return forms.ValidationError("password do not match")
		return pass2
	def save(self,commit=True):
		user = super(UserCreationForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user

class UserLoginForm(forms.Form):
	email = forms.EmailField(max_length=60,widget=forms.TextInput(attrs = {'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control'}))

	def clean(self,*args,**kargs):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		

