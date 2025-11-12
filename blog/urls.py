# blog/urls.py
from django.urls import path
from . import views # Importamos las vistas que acabamos de escribir

urlpatterns = [
    # path(URL, VISTA, NOMBRE_INTERNO)
    path('', views.inicio, name='inicio'), 
    path('autor/cargar/', views.cargar_autor, name='cargar_autor'),
    path('categoria/cargar/', views.cargar_categoria, name='cargar_categoria'),
    path('post/cargar/', views.cargar_post, name='cargar_post'),
    path('post/buscar/', views.busqueda_post, name='busqueda_post'),
]