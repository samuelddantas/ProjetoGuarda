from Show           import models
from django.forms   import ModelForm

# ======================================
# Todos os Forms Relacionados as Obras
# ======================================

class MidiaForm(ModelForm):
    class Meta:
        model = models.Midia
        fields = '__all__'

class GeneroForm(ModelForm):
    class Meta:
        model = models.Genero
        fields = '__all__'

class ObraForm(ModelForm):
    class Meta:
        model = models.Obra
        fields = '__all__'

class Genero_da_ObraForm(ModelForm):
    class Meta:
        model = models.Genero_da_Obra
        fields = '__all__'

# ======================================
# Todos os Forms Relacionados as Produções
# ======================================

class FuncionarioForm(ModelForm):
    class Meta:
        model = models.Funcionario
        fields = '__all__'

class FuncaoForm(ModelForm):
    class Meta:
        model = models.Funcao
        fields = '__all__'

class ProducaoForm(ModelForm):
    class Meta:
        model = models.Producao
        fields = '__all__'