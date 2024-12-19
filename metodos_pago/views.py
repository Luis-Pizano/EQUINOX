from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import MetodosPago
from .forms import MetodosPagoForm


def agregar_metodo_pago(request):
    if request.method == 'POST':
        form = MetodosPagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agrego exitosamente un nuevo metodo de pago')
            return redirect('listar_metodos_pago') 
    else:
        form = MetodosPagoForm()
    return render(request, 'agregar_metodos_pago.html', {'form': form})

def eliminar_metodo_pago(request,id):
    metodo = get_object_or_404(MetodosPago,id_metodo_pago=id)
    if request.method == 'POST':
       metodo.delete()
       messages.success(request, 'Metodo eliminado exitosamente')
       return redirect('listar_metodos_pago')
    else:
        messages.error(request,'Ocurrio un fallo al intentar eliminar el metodo de pago')
        return redirect('listar_metodos_pago')


def listar_metodos_pago(request):
    metodos = MetodosPago.objects.all()
    return render(request,'listar_metodos_pago.html', {"metodos":metodos})

def editar_metodo_pago(request, id):
    metodo_pago = get_object_or_404(MetodosPago, id_metodo_pago=id)

    if request.method == 'POST':
        form = MetodosPagoForm(request.POST, instance=metodo_pago)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Método de pago actualizado exitosamente.')
            return redirect('listar_metodos_pago')  
    else:
        form = MetodosPagoForm(instance=metodo_pago)

    return render(request, 'editar_metodo_pago.html', {'form': form})