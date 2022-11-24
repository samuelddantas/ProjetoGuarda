from django.contrib import admin

from .models import tipo_de_obra
from .models import obra
from .models import Classificacao

# Register your models here.

admin.site.register(tipo_de_obra)
admin.site.register(obra)
admin.site.register(Classificacao)