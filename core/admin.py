from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class ReservaAdmin(ImportExportModelAdmin):
    list_display = ['nombre', 'telefono','email','fecha','servi','tipo']
    search_fields = ['email','nombre']
    list_filter = ['tipo']
    list_per_page = 10

class ServicioAdmin(ImportExportModelAdmin):
    list_display = ['nombre','precio','tipo']

class CalificacionAdmin(ImportExportModelAdmin):
    list_display = ['nombre','comentario','nota']


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(TipoServicio)
admin.site.register(Calificacion,  CalificacionAdmin  )

