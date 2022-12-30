from django.contrib import admin
from Show           import models

# Obra
admin.site.register(models.Midia)
admin.site.register(models.Genero)
admin.site.register(models.Obra)
admin.site.register(models.Genero_da_Obra)
# Produção
admin.site.register(models.Funcionario)
admin.site.register(models.Funcao)
admin.site.register(models.Producao)