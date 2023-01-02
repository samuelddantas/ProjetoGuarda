from django.forms   import ModelForm
from django         import forms
from User           import models
from Show           import models as ShowModels

# ======================================
# Todos os Forms Relacionados aos Usuarios
# ======================================

class AssistidoForm(ModelForm):
    class Meta:
        model = models.Assistido
        fields = '__all__'


# class ReviewForm(ModelForm):
#     class Meta:
#         model = models.Review
#         fields = '__all__'

class ReviewForm(forms.Form):
    rev_review          = forms.CharField(label="Review", max_length=1000)
    
    classificacoes = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ]

    rev_classificacao   = forms.ChoiceField(label="CLassificação", choices=classificacoes)
    obr_obra            = forms.ModelChoiceField(label="Obra Assistida", queryset=ShowModels.Obra.objects.all())