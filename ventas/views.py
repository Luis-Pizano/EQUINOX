from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Ventas
from .forms import VentasForm

def agregar_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agregó exitosamente la venta.')
            return redirect('listar_ventas')
        else:
            messages.error(request,'Ocurrio un error al intetar agregar la venta.')
    else:
        form = VentasForm()
    return render(request,'agregar_ventas.html',{'form':form})

def listar_ventas(request):
    ventas = Ventas.objects.all()
    return render(request,'listar_ventas.html',{'ventas':ventas})

def eliminar_venta(request,id):
    venta = get_object_or_404(Ventas,id_venta=id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request,'Venta eliminada con exito')
    else:
        messages.error(request,'Ocurrio un fallo al intentar eliminar la venta')
    return redirect('listar_ventas')
