# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0007_remove_perfil_notificacoes'),
        ('notificacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='perfil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notificacao', to='perfis.Perfil'),
            preserve_default=False,
        ),
    ]
