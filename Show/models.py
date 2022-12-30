from django.db import models

# Todos os Modelos Relacionados as Obras

class Tipo(models.Model):
    tip_id  = models.AutoField(primary_key=True)
    tip_tipo = models.CharField(max_length=20)

class Genero(models.Model):
    gen_id  = models.AutoField(primary_key=True)
    gen_genero = models.CharField(max_length=20)

class Funcao(models.Model):
    fun_id = models.AutoField(primary_key=True)
    fun_funcao = models.CharField(max_length=50)

class Producao(models.Model):
    pro_id  = models.AutoField(primary_key=True)
    pro_nome  = models.ForeignKey
    pro_funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, default=1)

class Obra(models.Model):
    obr_id              = models.AutoField(primary_key=True)
    # obr_capa            = models.ImageField(height_field=100, width_field=100)
    obr_titulo          = models.CharField(max_length=100, verbose_name="Título")
    obr_sinopse         = models.CharField(max_length=500, verbose_name="Sinopse")
    obr_classificacao   = [
        ('L', 'Histórias sem conteúdos prejudiciais para qualquer infância'),
        ('10', 'Histórias com conteúdo violento e linguagem imprópria de nível leve'),
        ('12', 'Histórias com cenas de agressão física, insinuação de consumo de drogas e insinuação leve de sexo'),
        ('14', 'Histórias com agressão física média, consumo de drogas explícito e insinuação ao sexo moderada'),
        ('16', 'Histórias com consumo de drogas explícito, agressão física acentuada e insinuação de sexo acentuada'),
        ('18', 'Histórias com consumo e indução ao consumo de drogas, violência extrema, suícidio, cenas de sexo explícitas e distúbios psicossomáticos')
    ]

    obr_tipo            = models.ForeignKey(Tipo, on_delete=models.CASCADE, default=1)
    obr_genero          = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1)
    obr_producao        = models.ForeignKey(Producao, on_delete=models.CASCADE, default=1)