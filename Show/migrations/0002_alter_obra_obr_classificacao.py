# Generated by Django 4.1.4 on 2022-12-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='obr_classificacao',
            field=models.CharField(choices=[('L', 'L'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18')], default='L', max_length=2, verbose_name='Classificação Etária'),
        ),
    ]