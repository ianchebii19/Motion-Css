from . import views
from django.urls import path

urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('portfolio', views.portfolio , name='portfolio'),
    path('price/', views.price , name='price'),
    path('service/', views.service , name='service'),
    path('team/', views.team , name='team'),
 
  
    ]