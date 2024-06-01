"""
URL configuration for foodOdering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from home.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new , name="new"),
    path('home/', home , name="home"),
    # path('login/', loginPage , name="loginPage"),
    # path('sign/', register , name="register"),
    path('profile/', profilePage, name = 'profilePage'),
    path('login/', loginPage, name = 'loginPage'),
    path('sign/', register, name = 'register'),
    path('logout/', logOut, name = 'logOut'),
    path('edit/', edit, name = 'edit'),
    path('cart/', cart_view, name = 'cart_view'),
    # path('menu/', menu , name="menu"),
    # path('cart/', cart , name="cart"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
