# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Profile

# 1. Formulario para editar el modelo User (datos básicos)
class UserEditForm(forms.ModelForm):
    # Sobrescribimos el campo 'email' para que sea opcional, si es necesario
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        # Los campos 'first_name' y 'last_name' son los que pide la consigna (nombre, apellido)

# 2. Formulario para editar el modelo Profile (biografía, avatar)
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Usamos 'biografia' y 'avatar' que definimos en models.py
        fields = ['biografia', 'avatar']