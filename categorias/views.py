from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Categoria
from .forms import CategoriaForm

def agregar_categoria(request):
    if request.method == 'POST':
        form =CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se agrego una nueva categoria de forma exitosa')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request,'agregar_categoria.html',{'form':form})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request,'listar_categorias.html',{'categorias':categorias})

def eliminar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria eliminada exitosamente.')
        return redirect('listar_categorias')
    else:
        messages.error(request, 'Ocurrió un error al intentar eliminar la categoría.')
    return redirect('listar_categorias')


def editar_categoria(request, id):
    # Obtener la categoría por su ID
    categoria = get_object_or_404(Categoria, id_categoria=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        
        if form.is_valid():
            # Si el formulario es válido, guardamos la categoría
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'editar_categoria.html', {'form': form})