from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class ReservaAdmin(ImportExportModelAdmin):
    list_display = ['nombre', 'telefono','email','fecha','servi','tipo']
    search_fields = ['email','nombre']
    list_filter = ['tipo','fecha']
    list_per_page = 10

class ServicioAdmin(ImportExportModelAdmin):
    list_display = ['nombre','precio','tipo']
    search_fields = ['nombre']
    list_filter = ['tipo']

class CalificacionAdmin(ImportExportModelAdmin):
    list_display = ['nombre','comentario','nota']
    search_fields = ['nombre']
    list_filter = ['nota']

class blogPosteoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'post','fechaPost','imagenPost','autor','slug']
    search_fields = ['titulo','autor','fechaPost']
    list_filter = ['autor','fechaPost']


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(TipoServicio)
admin.site.register(Calificacion,  CalificacionAdmin  )
admin.site.register(BlogPost, blogPosteoAdmin)

