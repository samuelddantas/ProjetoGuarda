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
            'obr_titulo':           forms.TextInput                 (attrs={'class':'form-control'}),
            'obr_sinopse':          forms.Textarea                  (attrs={'class':'form-control'}),
            'obr_data':             forms.DateInput                 (attrs={
                'class':'form-control',
                'type': 'date',
            }),
            'obr_producao':         forms.Textarea                  (attrs={'class':'form-control'}),
            'obr_capa':             forms.URLInput                  (attrs={'class':'form-control'}),
            'obr_classificacao':    forms.RadioSelect               (attrs={'class':'form-control'}),
            'obr_mid_midia':        forms.Select                    (attrs={'class':'form-control'}),
            'obr_gen_genero':       forms.CheckboxSelectMultiple    (attrs={'class':'form-control'}),
        }

