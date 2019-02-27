"""django start up URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static

# This is the apps main urls section who maintain all the route
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('pages.urls')), # here we add or linking the urls.py in the pages app
    path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),# for accouts app where user can register and login
    path('contact/',include('contacts.urls')) # for contact app where user can make an in query

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
