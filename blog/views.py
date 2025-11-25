# blog/views.py
from django.shortcuts import render, redirect 
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm 
from .models import Post 
from django.db.models import Q # Necesario para construir consultas

# 1. Vista Principal (Home)
# Asegúrate de que esta función se llame 'inicio' y esté bien indentada.
def inicio(request): 
    return render(request, 'blog/index.html')


# 2. Vistas de Carga de Datos (3 Formularios)

def cargar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('inicio') 
    else:
        form = AutorForm() 
    
    return render(request, 'blog/form_general.html', {'form': form, 'titulo_form': 'Cargar Nuevo Autor'})

def cargar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    
    return render(request, 'blog/form_general.html', {'form': form, 'titulo_form': 'Cargar Nueva Categoría'})

def cargar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
    
    return render(request, 'blog/form_general.html', {'form': form, 'titulo_form': 'Cargar Nuevo Post'})


# 3. Vista de Búsqueda de Datos (1 Formulario de Búsqueda)

def busqueda_post(request):
    form = BusquedaPostForm(request.GET or None)
    resultados = []
    termino = None

    if form.is_valid():
        termino = form.cleaned_data.get('termino_busqueda')
        if termino:
            # Consulta: busca Posts cuyo título contenga el 'termino'
            resultados = Post.objects.filter(titulo__icontains=termino)
            
    return render(request, 'blog/busqueda.html', {'form': form, 'resultados': resultados, 'termino': termino})
# 4. Vista de Listado
def listar_posts(request):
    # Obtiene TODOS los objetos (registros) del modelo Post
    posts = Post.objects.all()
    
    # Envía la lista de posts al template 'listar_posts.html'
    return render(request, 'blog/listar_posts.html', {'posts': posts})
