from django.contrib import admin

from .models import PedidoAdocao


# Register your models here.

@admin.register(PedidoAdocao)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pet', 'usuario', 'status')
