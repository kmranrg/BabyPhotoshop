from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy-policy/', views.privacyPolicy, name='privacy-policy')
]