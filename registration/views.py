from django.shortcuts import render,redirect
from .forms import RegistrationForm,UserLoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from .models import MyUserManager,MyUser

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def index(request):
	return render(request,'registration/index.html')

def user_logout(request):
	logout(request)
	return redirect('/login/')

def user_register(request):
	if request.method == 'POST':
		user_form = RegistrationForm(request.POST)
		try:
			x=MyUser.objects.get(email=request.POST.get('email'))
			if x.is_active:
				pass
			else:
				x.delete()
		except MyUser.DoesNotExist:
			pass
		if user_form.is_valid():
			user = user_form.save()
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your FixMeet account.'
			message = render_to_string('registration/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),
			})
			to_email = user_form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')
			redirect('login')
		else:
			return render(request,'registration/register.html',
		                  {'form':user_form})

	user_form = RegistrationForm(request.POST)
	return render(request,'registration/register.html',
		                  {'form':user_form})



def user_login(request):
	if request.user.is_authenticated:
		return redirect("/home/")
	if request.method == 'POST':
		user_form = UserLoginForm(request.POST)
		if user_form.is_valid():
			user = authenticate(email = request.POST.get('email'),password = request.POST.get('password'))
			if user and user.is_active:
				login(request,user)
				return redirect('/home/')
			else:
				user_form=UserLoginForm()
				return render(request,'registration/login.html',{'form':user_form})

	user_form = UserLoginForm(request.POST)
	return render(request,'registration/login.html',
		                  {'form':user_form})
	

# Create your views here.
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

