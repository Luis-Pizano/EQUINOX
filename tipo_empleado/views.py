from django.shortcuts import get_object_or_404, render, redirect
from .models import TipoEmpleado
from .forms import TipoEmpleadoForm
from django.contrib import messages

def listar_tipo_empleados(request):
    tipos_empleados = TipoEmpleado.objects.all()
    context = {
        'tipos_empleados': tipos_empleados
    }
    return render(request, 'listar_tipo_empleados.html', context)

def agregar_tipo_empleado(request):
    if request.method == 'POST':
        form = TipoEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo tipo de empleado
            return redirect('listar_tipo_empleados')  # Redirigir a la lista después de guardar
    else:
        form = TipoEmpleadoForm() 

    context = {
        'form': form
    }
    return render(request, 'agregar_tipo_empleado.html', context)

def eliminar_tipo_empleado(request, tipo_empleado_id):
    tipo_empleado = get_object_or_404(TipoEmpleado, id_tipo_empleado=tipo_empleado_id)
    tipo_empleado.delete()
    messages.success(request, "Tipo de empleado eliminado con éxito.")
    return redirect('listar_tipo_empleados')

def editar_tipo_empleado(request, tipo_empleado_id):

    tipo_empleado = get_object_or_404(TipoEmpleado, id_tipo_empleado=tipo_empleado_id)
    if request.method == 'POST':
        form = TipoEmpleadoForm(request.POST, instance=tipo_empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de empleado actualizado exitosamente.')
            return redirect('listar_tipo_empleados')
    else:
        form = TipoEmpleadoForm(instance=tipo_empleado)

    return render(request, 'editar_tipo_empleado.html', {'form': form})




