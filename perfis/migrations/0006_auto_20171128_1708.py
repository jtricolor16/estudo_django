# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_perfil_notificacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='notificacoes',
            field=models.ManyToManyField(related_name='perfil', to='notificacao.Notificacao'),
        ),
    ]