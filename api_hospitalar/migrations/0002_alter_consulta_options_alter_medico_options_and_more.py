# Generated by Django 4.2.4 on 2023-08-23 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_hospitalar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consulta',
            options={'ordering': ['paciente']},
        ),
        migrations.AlterModelOptions(
            name='medico',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['nome']},
        ),
    ]