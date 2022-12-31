from django.db      import models
from django.conf    import settings
from Show.models    import Obra

# ======================================
# Todos os Modelos Relacionados aos Usuários
# ======================================

class Assistido(models.Model):
    ass_id = models.AutoField(primary_key=True)
    ass_obr_id = models.ForeignKey(Obra, on_delete=models.CASCADE, default=1, verbose_name="Obra")
    ass_use_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, verbose_name="Usuário") 

    class Meta:
        verbose_name        = "Obra Assistida"
        verbose_name_plural = "Obras Assistidas"

    def __str__(self):
        return "%s : %s" % (self.ass_obr_id, self.ass_use_id)

class Review(models.Model):
    rev_id = models.AutoField(primary_key=True)
    rev_review = models.CharField(max_length=1000, verbose_name="Review")
    
    classificacoes = [
        ('1','Estrela 1'),
        ('2','Estrela 2'),
        ('3','Estrela 3'),
        ('4','Estrela 4'),
        ('5','Estrela 5'),
    ]

    rev_classificacao = models.CharField(max_length=1, choices=classificacoes, verbose_name="Classificação")
    rev_ass_id = models.ForeignKey(Assistido, on_delete=models.CASCADE, default=1, verbose_name="Obra")

    class Meta:
        verbose_name        = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "%s Review" % (self.rev_ass_id)