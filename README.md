# EQUINOX instalar entorno virtual
# Instalar Django
# Instalar pillow
# Instalar mssql-django y configurarlo
# instalar el driver ODBC DRIVER 17
# Configuración:   

# DATABASES = {
#    'default': {
#        'ENGINE': 'mssql',
#        'NAME': 'EQUINOX',
#        'USER': 'ADMIN_EQUINOX',
#        'PASSWORD': '1234',
#        'HOST': 'host que utilizas',
#        'PORT': '',  # Deja vacío si usas el puerto por defecto (1433)
#        'OPTIONS': {
#            'driver': 'ODBC Driver 17 for SQL Server',
#        },
#   }
# }

# Este sitio web puede ser accedido desde moviles, pero solo esta optimizadas las paginas presentación_ejemplares, presentación_razas, detalle_ejemplares
# falta una buena optimización de la barra de navegación para que esta se adapte sin mayor problema a dispositvos moviles
# falta una forma de cambiar el status (0 o 1 dependiendo de la cuenta) de cada cuenta, cambiar este status por medio de la pagina web y no desde la base de datos con un update cuentas_account set 
