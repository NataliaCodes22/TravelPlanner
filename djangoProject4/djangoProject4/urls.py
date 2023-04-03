"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from TravelPlanner import views

app_name = 'TravelPlanner'

# noinspection PyRedeclaration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='homepage'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destination/<int:pk>/', views.destination_detail, name='destination_detail'),
    path('destination/create/', views.destination_create, name='destination_create'),
    path('travel-plans/', views.travel_plan_list, name='travel_plan_list'),
    path('travel-plan/add/', views.travel_plan_add, name='travel_plan_add'),
    path('travel-plan/<int:pk>/', views.travel_plan_detail, name='travel_plan_detail'),
    path('travel-plan/create/', views.travel_plan_create, name='travel_plan_create'),
    path('packing-list/add/', views.packing_list_add, name='packing_list_add'),
    path('packing-item/add/', views.packing_item_add, name='packing_item_add'),
    path('photo-upload/', views.photo_upload, name='photo_upload'),
    path('accounts/', include('django.contrib.auth.urls')),

]
