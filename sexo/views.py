from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from sexo.forms import SexoForm
from sexo.models import Sexo

def agregar_sexo(request):
    if request.method == 'POST':
        form = SexoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se agrego un nuevo sexo de forma exitosa')
            return redirect('listar_sexo')
    else:
        form = SexoForm()
    return render(request, 'agregar_sexo.html', {'form':form})
    
def listar_sexo(request):
    sexos = Sexo.objects.all().order_by('id_sexo')
    return render(request, 'listar_sexo.html', {'sexos': sexos})

def eliminar_sexo(request,id):
    sexo = get_object_or_404(Sexo,id_sexo=id)
    if request.method == 'POST':
       sexo.delete()
       messages.success(request, 'sexo eliminado exitosamente')
       return redirect('listar_sexo')
    else:
        messages.error(request,'Ocurrio un fallo al intentar eliminar el sexo')
        return redirect('listar_sexo')