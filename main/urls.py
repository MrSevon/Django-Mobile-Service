from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('services', views.services, name='services'),
    path('order/', views.order_view, name='order'),
    path('order/success/', views.order_success_view, name='order_success'),
]