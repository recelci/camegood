from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import (

	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView

	)

from .forms import ArticleModelForm

from .models import Article


# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# # Use the application default credentials

# cred = credentials.Certificate("static/admin/iyigeldi01-firebase-adminsdk-711gp-6c541affb0.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()


class ArticleCreateView(CreateView):

	template_name	= 'blog/article_create.html'  
	form_class		= ArticleModelForm
	queryset 		= Article.objects.all()

	def form_valid(self, form):
		print(form.cleaned_data)

		return super().form_valid(form)

@method_decorator(login_required(redirect_field_name=None), name='dispatch')
class ArticleListView(ListView):

	template_name	= 'blog/articles.html'
	queryset 		= Article.objects.all()


class ArticleDetailView(DetailView):

	template_name	= 'blog/article_detail.html'
	#queryset 		= Article.objects.all()    # filters etc.

	def get_object(self):

		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):

	template_name	= 'blog/article_create.html'
	form_class		= ArticleModelForm
	queryset 		= Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ArticleDeleteView(DeleteView):

	template_name	= 'blog/article_delete.html'
	#queryset 		= Article.objects.all()    # filters etc.

	def get_object(self):

		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('blog:article-list')