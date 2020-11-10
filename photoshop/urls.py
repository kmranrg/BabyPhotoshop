from  django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo_sharpness/', views.photo_sharpness, name='photo_sharpness'),
    path('photo_saturation/', views.photo_saturation, name='photo_saturation'),
    path('photo_transpose/', views.photo_transpose, name='photo_transpose')
]