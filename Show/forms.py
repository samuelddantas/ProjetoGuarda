from Show           import models
from django.forms   import ModelForm
from django         import forms

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

class ObraForm(forms.Form):
    obr_titulo          = forms.CharField(label="Título da Obra", max_length=100)
    obr_sinopse         = forms.CharField(label="Sinopse", max_length=500)
    obr_data            = forms.DateField(label="Data de Lançamento",widget=forms.DateInput(attrs={'type': 'date'}))

    classificacao       = [
        ('L' , 'L'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    ]

    obr_classificacao   = forms.ChoiceField(label="Classificação Indicativa",choices=classificacao)
    obr_mid_midia       = forms.ModelChoiceField(label="Mídia", queryset=models.Midia.objects.all())
    # Colocando os Gêneros
    gen_genero         = forms.ModelMultipleChoiceField(label="Gêneros", queryset=models.Genero.objects.all())
    # Colocando os Produtores
    

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