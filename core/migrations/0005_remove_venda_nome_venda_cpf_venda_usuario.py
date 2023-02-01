# Generated by Django 4.0.6 on 2023-01-27 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_venda_quantidade_entrada_pecas_valor_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='nome',
        ),
        migrations.AddField(
            model_name='venda',
            name='cpf',
            field=models.CharField(default=1, max_length=11, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venda',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
