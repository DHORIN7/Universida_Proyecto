from django.contrib import admin
from .models import Aspirante

# Register your models here.

class AspiranteAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Aspirante, AspiranteAdmin)