from django.forms   import ModelForm
from User           import models

# ======================================
# Todos os Forms Relacionados aos Usuarios
# ======================================

class AssistidoForm(ModelForm):
    class Meta:
        model = models.Assistido
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = '__all__'