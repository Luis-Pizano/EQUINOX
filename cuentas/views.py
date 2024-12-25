
from django.shortcuts import render, redirect
from django.contrib import auth,messages
from .forms import RegistarseForms
from .models import Account
from django.contrib.auth import authenticate, login

def registrarse(request):
    if request.method == 'POST':
        form = RegistarseForms(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login') 
        else:
            messages.error(request, 'Error en el registro. Verifica los datos ingresados.')
    else:
        form = RegistarseForms()

    return render(request, 'registrarse.html', {'form': form})

def iniciar_sesion(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Utilizamos authenticate para comprobar las credenciales
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.info(request,"Se ha iniciado sesion correctamente.")
            return redirect('home')

        else:
            messages.error(request, "Correo o contraseña incorrectos.")
    
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def listar_cuentas(request):
    cuentas = Account.objects.all()
    return render(request,'listar_cuentas.html',{'cuentas':cuentas})