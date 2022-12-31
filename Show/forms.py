from Show     import models
from django.forms   import ModelForm

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