from django.urls import path
from .views import (

	UserCreateView,
	UserLoginView,
	UserLogoutView,
	ProfileView,
	UserProfileView,


)

app_name = "user"

urlpatterns = [

	path('register/', UserCreateView.as_view(), name="register"),

	path('login/', UserLoginView.as_view(), name="login"),
	path('logout/', UserLogoutView.as_view(), name="logout"),
	path('profile/', ProfileView , name="profile"),

]