from django.urls import path
from . import views
from django.conf.urls import url

app_name="gapi"
urlpatterns = [
    path('add-appointment/', views.main,name="add-appointment"),
    url(r'^(?P<pk>\d+)/$', views.EventUpdate.as_view(), name='add')
]