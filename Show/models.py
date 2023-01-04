from django.db import models

# ======================================
# Todos os Modelos Relacionados as Obras
# ======================================

class Midia(models.Model):
    mid_id  = models.AutoField(primary_key=True)
    mid_midia = models.CharField(max_length=20, verbose_name="Mídia")

    def __str__(self):
        return self.mid_midia

class Genero(models.Model):
    gen_id  = models.AutoField(primary_key=True)
    gen_genero = models.CharField(max_length=20, verbose_name="Gênero")

    class Meta:
        verbose_name        = "Gênero"
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.gen_genero

class Obra(models.Model):
    obr_id              = models.AutoField(primary_key=True)
    obr_titulo          = models.CharField(max_length=100, verbose_name="Título")
    obr_sinopse         = models.TextField(verbose_name="Sinopse")
    obr_data            = models.DateField(verbose_name="Data de Lançamento")
    obr_producao        = models.TextField(verbose_name="Lista de Produtores")
    obr_capa            = models.CharField(max_length=500, verbose_name="Link da Capa")

    classificacao       = [
        ('L' , 'L'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
    ]

    obr_classificacao   = models.CharField(max_length=2, choices=classificacao, default='L', verbose_name="Classificação Etária")
    obr_mid_midia       = models.ForeignKey(Midia, on_delete=models.CASCADE, default=1, verbose_name="Mídia")
    obr_gen_genero      = models.ManyToManyField(Genero, verbose_name="Gêneros")

    def __str__(self):
        return self.obr_titulo

