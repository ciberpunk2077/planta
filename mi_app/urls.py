from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal
    path('presentacion/', views.presentacion, name='presentacion'), 
    path('datos/', views.datos, name='datos'), 
]