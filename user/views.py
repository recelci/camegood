from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import admin, messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
	
	LoginView,
	LogoutView

	)

from django.views.generic import (

	CreateView,
	DetailView,
	TemplateView

	)

from .forms import (

	UserRegisterForm,
	UserLoginForm,
	UserUpdateForm,
	ProfileUpdateForm

	)

from .models import Profile

# Create your views here.


class UserCreateView(CreateView):

	template_name	= 'user/register.html'  
	form_class		= UserRegisterForm

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):

		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account is created, now you can login! {username}')

			return redirect('user:login')

		return render(request, self.template_name, {'form': form})



class UserLoginView(LoginView):

	template_name	= 'user/login.html' 

	def redirect_authenticated_user(self):

		return reverse('blog:article-list')

	def get_success_url(self):

		return reverse('blog:article-list')




class UserLogoutView(LogoutView):

	template_name	= 'user/logout.html'  
	#queryset 		= Article.objects.all()


	# def form_valid(self, form):
	# 	print(form.cleaned_data)

	# 	return super().form_valid(form)

	def get_success_url(self):
		return reverse('home')


@login_required
def ProfileView(request):

	if request.method == 'POST':		
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
			request.FILES,
			instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your profile is updated! {request.user.username}')
			return redirect('user:profile')

	else :
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)


	context = {

		'u_form': u_form,
		'p_form': p_form

		}

	return render (request, 'user/profile.html', context)


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):

	template_name	= 'user/profile.html'  

	def ProfileView(request):
		return render (request, self.template_name)