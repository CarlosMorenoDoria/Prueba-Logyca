"""Punto345 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import  path
from Punto3 import views as vie
from Punto4 import views as view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name='home'),
    path('numeroprimo', vie.numeroprimo, name='numeroprimo'),
    path('primosgemelos', vie.primosgemelos, name='primosgemelos'),
    path('numerosprimos', view.numerosprimos, name='numerosprimos'),
    path('primogemelos', view.primogemelos, name='primogemelos'),
]
