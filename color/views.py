from django.shortcuts import get_object_or_404, redirect, render
from color.forms import ColorForm
from django.contrib import messages
from .models import Color

def agregar_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se agrego exitosamente un nuevo color ')
            return redirect('listar_colores')
    else:
        form = ColorForm()
    return render(request,'agregar_color.html',{'form':form})

def listar_color(request):
    colores = Color.objects.all()
    return render(request,'listar_colores.html',{'colores':colores})

def eliminar_color(request, id):
    color = get_object_or_404(Color, id_color=id)
    if request.method == 'POST': 
        color.delete()
        messages.success(request, 'Color eliminado exitosamente.')
        return redirect('listar_colores')  
    else:
        messages.error(request,'Ocurrio un error al intentar eliminar el color')
    return render(request, 'listar_color.html')