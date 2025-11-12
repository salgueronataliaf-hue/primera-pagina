# blog/forms.py
from django import forms
# Importamos las clases que definimos en models.py
from .models import Autor, Categoria, Post 

# 1. Formulario para la clase Autor (ModelForm para cargar datos)
class AutorForm(forms.ModelForm):
    class Meta:
        # Indicamos que este formulario se basa en el modelo Autor
        model = Autor
        # Indicamos qué campos del modelo queremos que aparezcan en el formulario
        fields = ['nombre', 'apellido', 'email'] 

# 2. Formulario para la clase Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

# 3. Formulario para la clase Post (Incluye los desplegables de Autor y Categoría)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'categoria']
        # Nota: 'autor' y 'categoria' aparecerán automáticamente como menús desplegables 
        # para que el usuario pueda seleccionar los datos previamente cargados.

# 4. Formulario para Buscar Algo en la BD (Cumple el requisito de búsqueda)
class BusquedaPostForm(forms.Form):
    # Esto no se basa en un modelo, solo en un campo simple de texto
    termino_busqueda = forms.CharField(label='Buscar Post por Título', max_length=100, required=False)