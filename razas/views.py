from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Razas
from .forms import RazasForm, RazasFormEditar
from django.core.paginator import Paginator


def listar_razas(request):
    razas = Razas.objects.all()
    return render(request, 'listar_razas.html', {'razas':razas})

def agregar_raza(request):
    if request.method == 'POST':
        form = RazasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agrego exitosamente una nueva raza')
            return redirect('listar_razas')
        else:
            messages.error(request,'Ocurrio un error al intentar agregar la raza')
    else:
        form = RazasForm()
    return render(request, 'agregar_razas.html', {'form': form}) 

def eliminar_raza(request, id):
    raza = get_object_or_404(Razas, id_raza=id)
    if request.method == 'POST': 
        raza.delete()
        messages.success(request, 'Raza eliminada exitosamente.')
    return redirect('listar_razas')

    
def presentacion_razas(request):
    imagenes = Razas.objects.all()
    cantidad_razas = razas_page(request,imagenes,4)
    return render(request, 'presentacion_razas.html', {'imagenes':cantidad_razas})

def editar_raza(request, id_raza):
    raza = get_object_or_404(Razas, id_raza=id_raza)  # Obtén la raza o muestra un 404 si no existe
    if request.method == 'GET':
        form = RazasFormEditar(request.GET, instance=raza)
        if form.is_valid():
            form.save()
            messages.success(request, 'Raza actualizada exitosamente.')
            return redirect('listar_razas')
    else:
        form = RazasFormEditar(instance=raza)
    # Envía 'raza' al contexto
    return render(request, 'editar_raza.html', {'form': form, 'raza': raza})


def razas_page(request,ejemplares,ejemplares_by_page):
    paginator = Paginator(ejemplares,ejemplares_by_page)
    pagina = request.GET.get('pagina')
    pagina_ejemplares = paginator.get_page(pagina)
    return pagina_ejemplares
