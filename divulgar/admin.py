from django.contrib import admin

from .models import Pet, Raca, Tag

# Register your models here.

admin.site.register(Raca)
admin.site.register(Tag)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'usuario')
    prepopulated_fields = {'slug': ('nome',)}
