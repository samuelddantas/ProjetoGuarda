# Generated by Django 4.1.3 on 2022-11-24 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guarda', '0003_merge_20220908_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificacao',
            name='nome',
            field=models.CharField(max_length=20, verbose_name='Nome da Classificação'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='autor',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Diretor/Autor da obra'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='classificacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guarda.classificacao', verbose_name='Classificação'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='foto',
            field=models.CharField(max_length=300, verbose_name='Foto (url)'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome da obra'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='observacao',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='sinopse',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Sinopse da obra'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='tipo_de_obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guarda.tipo_de_obra', verbose_name='Tipo de obra'),
        ),
        migrations.AlterField(
            model_name='tipo_de_obra',
            name='foto_obra',
            field=models.CharField(max_length=300, null=True, verbose_name='Foto (url)'),
        ),
        migrations.AlterField(
            model_name='tipo_de_obra',
            name='nome',
            field=models.CharField(max_length=45, verbose_name='Nome do tipo de obra'),
        ),
    ]
