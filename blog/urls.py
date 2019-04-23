from django.urls import path
from .views import (

	ArticleCreateView,
	ArticleDetailView,
	ArticleListView,
	ArticleUpdateView,
	ArticleDeleteView

)

app_name = "blog"

urlpatterns = [

	path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('', ArticleListView.as_view(), name="article-list"),
    path('<int:id>/detail/', ArticleDetailView.as_view(), name="article-detail"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article-delete"),

]