from django.contrib import admin
# Register your models here.
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'username', 'first_name', 'last_name','is_staff')
