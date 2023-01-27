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

class ObraForm(ModelForm):
    class Meta:
        model = models.Obra
        fields = '__all__'
        # Serve para Editar o Tipo de Campo, Classes e Id.
        widgets = {
            'obr_titulo':           forms.TextInput                 (attrs={
                'class':'sign__input',
                'placeholder': 'Título da Obra'
            }),
            'obr_sinopse':          forms.Textarea                  (attrs={
                'class':'sign__input',
                'placeholder': 'Sinopse'
            }),
            'obr_data':             forms.DateInput                 (attrs={
                'class':'sign__input',
                'placeholder': 'Data',
                'type': 'date',
            }),
            'obr_producao':         forms.Textarea                  (attrs={
                'class':'sign__input',
                'placeholder': 'Produtores'
            }),
            'obr_capa':             forms.URLInput                  (attrs={
                'class':'sign__input',
                'placeholder': 'Link da Capa'
            }),
            'obr_classificacao':    forms.Select               (attrs={
                'class':'sign__input',
                'placeholder': 'Classificação'
            }),
            'obr_mid_midia':        forms.Select                    (attrs={
                'class':'sign__input',
                'placeholder': 'Tipo de Mídia'
            }),
            'obr_gen_genero':       forms.SelectMultiple    (attrs={
                'class':'sign__input',
                'placeholder': 'Gênero da Obra',
                'style': "height: auto;",
            }),
        }

