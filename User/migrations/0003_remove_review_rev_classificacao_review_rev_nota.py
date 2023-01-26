# Generated by Django 4.1.4 on 2023-01-04 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_remove_review_rev_ass_id_review_rev_obr_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rev_classificacao',
        ),
        migrations.AddField(
            model_name='review',
            name='rev_nota',
            field=models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Nota'),
        ),
    ]