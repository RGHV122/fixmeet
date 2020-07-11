"""fixmeet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from registration import views as v
import django.contrib.auth.views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('registration.urls')),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        v.activate, name='activate'),
    
    path('google/',include('calendarapi.urls')),

    
   
    url('^home/change-password/$', auth_views.password_change, {'post_change_redirect': '/home/'}, name='password_change'),
     path('home/',include('main.urls')),
     path('myprofile/',include('main.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
