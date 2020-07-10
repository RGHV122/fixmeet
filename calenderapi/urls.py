from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('add-appointment/', views.main),
    url(r'^(?P<pk>\d+)/$', views.EventUpdate.as_view(), name='add')
]