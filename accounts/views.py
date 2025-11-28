# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import UserEditForm, ProfileEditForm 
from .models import Profile 

# VISTA DE REGISTRO (SIGNUP)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Loguear al usuario inmediatamente después del registro
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}! Registro exitoso.")
            return redirect('inicio') 
        else:
            messages.error(request, "Error en el formulario de registro.")
    else:
        form = UserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})

# VISTA DE LOGIN
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido de vuelta, {username}!")
                return redirect('inicio')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# VISTA DE LOGOUT
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('inicio')
@login_required # Solo usuarios logueados pueden acceder
def profile_view(request):
    # El perfil se recupera automáticamente gracias al signal
    return render(request, 'accounts/profile_view.html')


# VISTA DE EDICIÓN DE PERFIL (Update profile)
@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user) 

    if request.method == 'POST':
        # Instanciamos los formularios con los datos POST y los archivos (FILES)
        user_form = UserEditForm(request.POST, instance=request.user)
        # IMPORTANTE: Pasamos instance=profile y request.FILES para la imagen/avatar
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            return redirect('profile_view') # Redirige a la vista del perfil
        else:
            messages.error(request, 'Error al actualizar tu perfil.')
    else:
        # Petición GET: Mostramos los formularios con los datos actuales
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 
                  'accounts/profile_edit.html', 
                  {'user_form': user_form, 'profile_form': profile_form})