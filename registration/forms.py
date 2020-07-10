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
	 ("","Gender"),
	('M','Male'),
	('F','Female'),
	('T','Transgender'),
]
class RegistrationForm(UserCreationForm):
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs = {'class':'text-input','placeholder':'Password'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs = {'class':'text-input','placeholder':'Re-type password'}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs = {'placeholder':'Email','class':'text-input'}))
	title= forms.CharField(label='',widget=forms.TextInput(attrs={'id':'title','class':'text-input','placeholder':"Title"}))
	gender= forms.CharField(label='', widget=forms.Select(choices=GENDER_CHOICES ,attrs={'id':'gender','class':'text-input'}))
	name = forms.CharField(label='', widget=forms.TextInput(attrs = {'class':'text-input','placeholder':'Name'}))
	class Meta:
		model = get_user_model()
		fields = ['name','email','title','gender']
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
	email = forms.EmailField(label='',max_length=60,widget=forms.TextInput(attrs = {'class':'text-input','placeholder':'Email'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs = {'id':'password','class':'text-input','placeholder':
		'Password'}))

	def clean(self,*args,**kargs):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		

