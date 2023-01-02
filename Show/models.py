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
    obr_sinopse         = models.CharField(max_length=500, verbose_name="Sinopse")
    obr_data            = models.DateField(verbose_name="Data de Lançamento")

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
    # obr_capa            = models.ImageField(height_field=100, width_field=100)

    def __str__(self):
        return self.obr_titulo

class Genero_da_Obra(models.Model):
    geo_id = models.AutoField(primary_key=True)
    geo_obr_obra = models.ForeignKey(Obra, on_delete=models.CASCADE, default=1, verbose_name="Obra")
    geo_gen_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1, verbose_name="Gênero")

    class Meta:
        verbose_name        = "Gênero da Obra"
        verbose_name_plural = "Gêneros da Obra"

    def __str__(self):
        return "%s / %s" % (self.geo_obr_obra, self.geo_gen_genero)

# ============================================
# Todos os Modelos Relacionados aos Produtores
# ============================================

class Funcionario(models.Model):
    fun_id = models.AutoField(primary_key=True)
    fun_nome = models.CharField(max_length=50, verbose_name="Nome", blank=True)

    def __str__(self):
        return self.fun_nome

class Funcao(models.Model):
    fuc_id = models.AutoField(primary_key=True)
    fuc_funcao = models.CharField(max_length=50, verbose_name="Função", blank=True)

    class Meta:
        verbose_name        = "Função"
        verbose_name_plural = "Funções"

    def __str__(self):
        return self.fuc_funcao

class Producao(models.Model):
    pro_id                  = models.AutoField(primary_key=True)
    pro_fun_funcionario     = models.ForeignKey(Funcionario, on_delete=models.CASCADE, default=1, verbose_name="Funcionário")
    pro_fuc_funcao          = models.ForeignKey(Funcao, on_delete=models.CASCADE, default=1, verbose_name="Função")
    pro_obr_obra            = models.ForeignKey(Obra, on_delete=models.CASCADE, default=1, verbose_name="Obra")

    class Meta:
        verbose_name        = "Produção"
        verbose_name_plural = "Produtores"

    def __str__(self):
        return "%s - %s em %s" % (self.pro_fun_funcionario, self.pro_fuc_funcao, self.pro_obr_obra)

