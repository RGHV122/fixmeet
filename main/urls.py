
from django.urls import path,include
from . import views
app_name = 'main'

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('profile/<int:userid>',views.profile,name='profile'),
    path('book-appointment/',views.book_appointments,name='book-appointments'),
    path('my-appointment/',views.my_appointments,name='my-appointments'),
    path('change-password/',views.change_password,name='change-password'),
    path('add-slot/',views.add_slot,name='add-slot'),
   
]
