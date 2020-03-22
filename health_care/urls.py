"""health_care URL Configuration

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
from django.urls import path
from myChart import views as mychart_views
from WasteManagement import views as waste_views

urlpatterns = [
    path('myChart/', mychart_views.base, name='mychart_home'),
    path('waste/', waste_views.base, name='waste_home'),
    path('waste/all', waste_views.all_waste, name='all_waste'),
    path('admin/', admin.site.urls)
]
