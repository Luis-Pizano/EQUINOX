from django.shortcuts import get_object_or_404,redirect, render
from django.contrib import messages
from .models import TipoProveedor
from .forms import TipoProveedorForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import TipoProveedor
from .forms import TipoProveedorForm

def agregar_tipo_proveedor(request):
    if request.method == 'POST':
        form = TipoProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se agregó exitosamente un nuevo tipo de proveedor')
            return redirect('listar_tipo_proveedor')
        else:
            messages.error(request, 'Ocurrió un error al intentar agregar el tipo de proveedor')
    else:
        form = TipoProveedorForm()

    return render(request, 'agregar_tipo_proveedor.html', {'form': form})

def listar_tipo_proveedor(request):
    tipos = TipoProveedor.objects.all()
    return render(request,'listar_tipo_proveedor.html',{'tipos':tipos})

def eliminar_tipo_proveedor(request, tipo_proveedor_id): 
    tipo = get_object_or_404(TipoProveedor, id_tipo_proveedor=tipo_proveedor_id)
    tipo.delete()
    messages.success(request, 'Tipo de proveedor eliminado con éxito')
    return redirect('listar_tipo_proveedor')