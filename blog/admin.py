from django.contrib import admin

from .models import *


# Registramos cada modelo

admin.site.register(Personal)
admin.site.register(Interno)
admin.site.register(Historial_medico)
admin.site.register(Medicamento)
admin.site.register(Doctor)
admin.site.register(Habitacion)
admin.site.register(Mensualidad)
