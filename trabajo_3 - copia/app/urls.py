from django.urls import path
from . import views

urlpatterns = [
    path('', views.informacion, name='informacion'),
    path('producto/', views.producto, name='producto'),
   
]