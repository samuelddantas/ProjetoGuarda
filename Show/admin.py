from django.contrib import admin
from Show           import models

# Register your models here.
admin.site.register(models.Tipo)
admin.site.register(models.Genero)
admin.site.register(models.Funcao)
admin.site.register(models.Producao)
admin.site.register(models.Obra)