from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Ejemplares
from .forms import EjemplaresEditForm, EjemplaresForm
from carrito.models import Cart, CartItem
from django.core.paginator import Paginator

def agregar_ejemplar(request):
    if request.method == 'POST':
        form = EjemplaresForm(request.POST, request.FILES) # sin request.FILES, Django tomara el input image como campo vacio sin importar si la imagen es cargada
        if form.is_valid():
            form.save()
            messages.success(request, 'Ejemplar agregado exitosamente.')
            return redirect('listar_ejemplares')
        else:
            messages.error(request, 'Ocurrió un error al intentar agregar el ejemplar.')
    else:
        form = EjemplaresForm()
    return render(request, 'agregar_ejemplares.html', {'form': form})


def listar_ejemplares(request):
    ejemplares = Ejemplares.objects.all()
    return render(request,'listar_ejemplares.html',{'ejemplares':ejemplares})

def eliminar_ejemplar(request,id):
    ejemplar = get_object_or_404(Ejemplares,id_ejemplar=id)
    if request.method == 'POST':
        ejemplar.delete()
        messages.success(request,'Ejemplar eliminado exitosamente.')
    return redirect('listar_ejemplares')

def presentacion_ejemplares(request):
    imagenes = Ejemplares.objects.all()
    cantidad_ejemplares = ejemplares_page(request,imagenes,4)
    return render(request,'presentacion_ejemplares.html',{'imagenes':cantidad_ejemplares})

def detalle_ejemplar(request, id_ejemplar):
    ejemplar = Ejemplares.objects.get(id_ejemplar=id_ejemplar)
    in_cart = False

    try:
        cart = Cart.objects.get(cart_id=request.session.session_key)
        in_cart = CartItem.objects.filter(cart=cart, ejemplar=ejemplar).exists() #filtar por el id del carrito y id de ejemplar, SI ejemplar existe en ese carrito entonces in_cart no seria false
    except Cart.DoesNotExist:
        pass

    return render(request, 'detalle_ejemplares.html', {
        'ejemplar': ejemplar,
        'in_cart': in_cart
    })


def editar_ejemplar(request, id_ejemplar):
    ejemplar = get_object_or_404(Ejemplares, id_ejemplar=id_ejemplar)

    if request.method == 'GET':
        form = EjemplaresEditForm(request.GET,request.FILES, instance=ejemplar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ejemplar actualizado exitosamente.')
            return redirect('listar_ejemplares')
    else:
        form = EjemplaresEditForm(instance=ejemplar)

    return render(request, 'editar_ejemplar.html', {'form': form})

def buscador(request):
    query = request.GET.get('q', '')
    if query:
        resultados = Ejemplares.objects.filter(id_raza__nombre_raza__icontains=query)
    else:
        resultados = Ejemplares.objects.none()
    
    return render(request, 'buscador.html', {'resultados': resultados, 'query': query})


# ================== FUNCION DE PAGINACION ==================
def ejemplares_page(request,ejemplares,ejemplares_by_page):
    paginator = Paginator(ejemplares,ejemplares_by_page)
    pagina = request.GET.get('pagina')
    pagina_ejemplares = paginator.get_page(pagina)
    return pagina_ejemplares
    
    
