from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .forms import TipoSuministroForm
from .models import TipoSuministro


def agregar_tipo_suministro(request):
    if request.method =='POST':
        form = TipoSuministroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agregó exitosamente un nuevo tipo de suministro')
            return redirect('listar_tipo_suministro')
        else:
            messages.error(request, 'Ocurrió un error al intentar agregar el tipo de suministro')
    else:
        form = TipoSuministroForm()
    return render(request,'agregar_tipo_suministro.html',{'form':form})

def listar_tipo_suministro(request):
    tipos = TipoSuministro.objects.all()
    return render(request,'listar_tipo_suministro.html',{'tipos':tipos})

def eliminar_tipo_suminstro(request, tipo_suministro_id):
    tipo = get_object_or_404(TipoSuministro, id_tipo_suministro=tipo_suministro_id)
    tipo.delete()
    messages.success(request, 'Tipo de suministro eliminado con éxito')
    return redirect('listar_tipo_suministro')


def editar_tipo_suministro(request, id):
    tipo_suministro = get_object_or_404(TipoSuministro, id_tipo_suministro=id)

    if request.method == 'POST':
        form = TipoSuministroForm(request.POST, instance=tipo_suministro)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de suministro actualizado exitosamente.')
            return redirect('listar_tipo_suministro')
    else:
        form = TipoSuministroForm(instance=tipo_suministro)

    return render(request, 'editar_tipo_suministro.html', {'form': form})

