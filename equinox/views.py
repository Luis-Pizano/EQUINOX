from django.shortcuts import render
from ejemplares.models import Ejemplares
from empleados.models import Empleado
from razas.models import Razas
from tipo_empleado.models import TipoEmpleado


def home(required):
    tipos_empleados = TipoEmpleado.objects.count()
    empleados = Empleado.objects.count()
    razas = Razas.objects.count()
    ejemplares = Ejemplares.objects.count()
    context = {
        "empleados": empleados,
        "tipos_empleados": tipos_empleados,
        "razas": razas,
        "ejemplares": ejemplares
    }
    return render(required,'home.html', context)

