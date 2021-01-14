from django.contrib import admin
from apps.principal.models import Equipo,Direccion,Relacion,Perfil
# Register your models here.


#configuraciondel panel de administrador
title = "Proyecto Django"
subtitle = "Panel de Gestion"

admin.site.register(Equipo)
admin.site.register(Direccion)
admin.site.register(Relacion)
admin.site.register(Perfil)