from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import Clientes
from .forms import ClientesForm, ClientesFormEditar

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cliente agregado exitosamente.')
            return redirect('listar_clientes')
        else:
            messages.error(request,'Ocurrio un error al intentar agregar al cliente.')
    else:
        form = ClientesForm()
    return render(request,'agregar_clientes.html',{'form':form})

def listar_cliente(request):
    clientes = Clientes.objects.all()
    return render(request,'listar_clientes.html',{'clientes':clientes})

def eliminar_cliente(request,id):
    cliente = get_object_or_404(Clientes,id_cliente = id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request,'Cliente eliminado exitosamente.')
        return redirect('listar_clientes')
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar al cliente.')
    return render(request,'listar_clientes.html',)

def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)

    if request.method == 'POST':
        form = ClientesFormEditar(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('listar_clientes')  # Asegúrate de tener la URL para listar los clientes
    else:
        form = ClientesForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form})