# accounts/urls.py 
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'), 
    
    # NUEVAS RUTAS DE PERFIL
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]