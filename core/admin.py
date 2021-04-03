from django.contrib import admin

from .models import Cliente, Etapa,Experto,Inversion,Inversionista,Proyecto,Tipo
admin.site.register(Cliente)
admin.site.register(Etapa)
admin.site.register(Experto)
admin.site.register(Inversion)
admin.site.register(Inversionista)
admin.site.register(Proyecto)
admin.site.register(Tipo)

