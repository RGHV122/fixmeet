
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('set-free-hour/',views.set_free_hour,name='set-free-hour'),
    path('search/<str:name>/',views.search,name='search'),
    path('search/',views.search,name='search'),
    path('profile/<int:userid>',views.profile,name='profile'),
    path('book-appointment/',views.book_appointments,name='profile'),
    path('my-appointment/',views.my_appointments,name='profile'),
   
]
