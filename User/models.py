from django.db      import models
from django.conf    import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from Show.models    import Obra

# ======================================
# Todos os Modelos Relacionados aos Usuários
# ======================================

class Review(models.Model):
    rev_id      = models.AutoField(primary_key=True)
    rev_obr_id  = models.ForeignKey(Obra, on_delete=models.CASCADE, default=1, verbose_name="Obra")
    rev_use_id  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, verbose_name="Usuário") 
    rev_review  = models.TextField(verbose_name="Review")
    rev_nota    = models.FloatField(verbose_name="Nota", default=1, validators=[
        MaxValueValidator(10),
        MinValueValidator(0),
    ])

    class Meta:
        verbose_name        = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "%s Review por %s" % (self.rev_obr_id, self.rev_use_id)