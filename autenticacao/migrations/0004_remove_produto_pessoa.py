# Generated by Django 4.1 on 2022-08-27 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_prestacaoservico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='pessoa',
        ),
    ]
