from django.db import models

from django.db import models # type: ignore
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # type: ignore

class MyAccountManager(BaseUserManager):
    def create_user(self, nombre, apellido, usuario, email, password=None):
        if not email:
            raise ValueError("Debe ingresar un correo")
        if not usuario:
            raise ValueError("Debe tener un nombre de usuario")
        user = self.model(
            email=self.normalize_email(email),
            usuario=usuario,
            nombre=nombre,
            apellido=apellido,
        )
        
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, usuario, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            usuario=usuario,
            password=password,
            nombre=nombre,
            apellido=apellido,
        )
        user.is_admin = True
        user.is_active = True
        user.lectura = True
        user.escritura = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    numero_telefono = models.CharField(max_length=50)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_cuidador = models.BooleanField(default=False)
    is_criador = models.BooleanField(default=False)
    is_veterinario = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario', 'nombre', 'apellido']
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    # Asignar el administrador personalizado
    objects = MyAccountManager()

