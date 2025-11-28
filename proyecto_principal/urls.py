# proyecto_principal/urls.py

from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # 1. Ruta de Administración
    path('admin/', admin.site.urls),
    
    # 2. Ruta de la Aplicación Blog
    path('', include('blog.urls')),
    
    # 3. Rutas de Autenticación de tu App (login, register, profile)
    path('accounts/', include('accounts.urls')),
    
    # 4. Rutas de Autenticación de Django (password change, password reset)
    path('accounts/', include('django.contrib.auth.urls')), 
]

# Configuración para servir archivos media (imágenes subidas por el usuario) en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)