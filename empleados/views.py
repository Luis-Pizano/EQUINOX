from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado agregado exitosamente.')
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'agregar_empleado.html', {'form': form})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == 'POST': 
        empleado.delete()
        messages.success(request, 'Empleado eliminado exitosamente.')
    return redirect('listar_empleados')  


def editar_empleado(request, id):
    # Obtener el empleado seleccionado
    empleado = get_object_or_404(Empleado, id_empleado=id)
    
    if request.method == 'POST':
        # Pasar los datos del formulario para la edición
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()  # Guardar los nuevos datos del empleado
            messages.success(request, 'Empleado actualizado exitosamente.')
            return redirect('listar_empleados')  # Redirigir a la lista de empleados
    else:
        # Pre-cargar el formulario con los datos del empleado actual
        form = EmpleadoForm(instance=empleado)
    
    return render(request, 'editar_empleado.html', {'form': form})
