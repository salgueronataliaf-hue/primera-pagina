# proyecto_principal/urls.py
from django.contrib import admin
from django.urls import path, include 
urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea redirige todo el tráfico de la raíz (/) a las URLs de la app 'blog'
    path('', include('blog.urls')), 
]
