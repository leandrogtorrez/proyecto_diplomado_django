from django.contrib import admin

from .models import Empleado, Departamento, Proyecto, Asignacion
# Register your models here.

admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Proyecto)
admin.site.register(Asignacion)
