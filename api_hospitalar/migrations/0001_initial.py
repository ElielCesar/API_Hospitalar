# Generated by Django 4.2.4 on 2023-08-22 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api_hospitalar.pessoa')),
                ('especializacao', models.CharField(max_length=200)),
                ('crm', models.CharField(max_length=200)),
            ],
            bases=('api_hospitalar.pessoa',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api_hospitalar.pessoa')),
                ('procedimento_medico', models.CharField(max_length=200)),
            ],
            bases=('api_hospitalar.pessoa',),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateTimeField(auto_now_add=True)),
                ('diagnostico', models.CharField(max_length=400)),
                ('prescricao', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_hospitalar.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_hospitalar.paciente')),
            ],
        ),
    ]
