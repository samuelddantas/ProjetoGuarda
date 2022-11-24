from django.db import models

# Create your models here.

class tipo_de_obra(models.Model):
    nome = models.CharField(max_length=45, verbose_name='Nome do tipo de obra')
    data_criacao = models.DateField(auto_now_add=True)
    foto_obra = models.CharField(max_length=300, null=True, verbose_name='Foto (url)')

    class Meta:
        verbose_name_plural = 'tipos de obras'
        
    def __str__(self):
        return self.nome

class Classificacao(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome da Classificação')
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'classificacoes'
    
    def __str__(self):
        return self.nome

class obra(models.Model):
    nome = models.CharField(max_length=100, verbose_name= 'Nome da obra')
    autor = models.CharField(max_length=45, null=True, blank=True, verbose_name='Diretor/Autor da obra')
    sinopse = models.CharField(max_length=300, null=True, blank=True, verbose_name='Sinopse da obra')
    tipo_de_obra = models.ForeignKey (tipo_de_obra, on_delete= models.CASCADE, verbose_name='Tipo de obra')
    classificacao = models.ForeignKey (Classificacao, on_delete= models.CASCADE, verbose_name='Classificação')
    observacao = models.CharField(max_length=200, null=True, blank=True, verbose_name='Observação')
    foto = models.CharField(max_length=300, verbose_name= 'Foto (url)')
    class Meta:
        verbose_name_plural = 'obras'
    
    def __str__(self):
        return self.nome
