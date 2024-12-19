from django.shortcuts import get_object_or_404,redirect,render
from django.contrib import messages
from .models import PedigreeEjemplar
from .forms import PedigreeEjemplarForm

def agregar_pedigree(request):
    if request.method == 'POST':
        form = PedigreeEjemplarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se agrego un nuevo pedigree de forma exitosa')
            return redirect('listar_pedigree')
    else:
        form = PedigreeEjemplarForm()
    return render(request,'agregar_pedigree.html',{'form':form})

def listar_pedigree(request):
    pedigrees = PedigreeEjemplar.objects.all()
    return render(request,'listar_pedigree.html',{'pedigrees':pedigrees})

def eliminar_pedigree(request,id):
    pedigree = get_object_or_404(PedigreeEjemplar,id_pedigree = id)
    if request.method == 'POST':
        pedigree.delete()
        messages.success(request, 'Pedigree eliminado exitosamente.')
        return redirect('listar_pedigree')
    else:
        messages.error(request, 'Ocurrió un error al intentar eliminar el pedigree.')
    return redirect('listar_pedigree')