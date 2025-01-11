from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agrego exitosamente un nuevo proveedor')
            return redirect('listar_proveedores')
        else:
            messages.error(request,'Ocurrio un error al intentar agregar el proveedor')
    else:
        form = ProveedorForm()
    return render(request,'agregar_proveedor.html',{'form':form})

def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request,'listar_proveedores.html',{'proveedores':proveedores})

def eliminar_proveedor(request,id):
    proveedor = get_object_or_404(Proveedor,id_proveedor = id)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request,'Proveedor eliminado exitosamente')
        return redirect('listar_proveedores')
    
def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == 'GET':
        form = ProveedorForm(request.GET, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamente.')
            return redirect('listar_proveedores')
        else:
            messages.error(request, 'Ocurrió un error al intentar actualizar el proveedor.')
    else:
        form = ProveedorForm(instance=proveedor)
    
    return render(request, 'editar_proveedor.html', {'form': form})
