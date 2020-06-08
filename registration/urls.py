from django.urls import path,include
from . import views
app_name = 'registration'

urlpatterns = [
	path('', views.index,name='index'),
    path('login/', views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('logout/',views.user_logout,name='logout')
]
