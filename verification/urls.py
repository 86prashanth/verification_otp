"""
URL configuration for verification project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from verify_app.views import *
from todo_mail.views import *
from Verification_Otp.views import send_otp,verify_otp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('send_otp/',send_otp,name='send_otp'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('login/',auth_view,name='auth'),
    path('verify/',verify_view,name='verify'),
    path('create/',todo_create,name='create'),
]
