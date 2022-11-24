from django.forms import ModelForm

from .models import tipo_de_obra
from .models import Classificacao
from .models import obra

class tipo_de_obraForm(ModelForm):
    class Meta:
        model = tipo_de_obra
        fields = ['nome','foto_obra']

class ClassificacaoForm(ModelForm):
    class Meta:
        model = Classificacao
        fields = ['nome']

class obraForm(ModelForm):
    class Meta:
        model = obra
        fields = ['nome','autor','sinopse','tipo_de_obra','classificacao','observacao', 'foto']
    

