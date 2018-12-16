# Generated by Django 2.1.4 on 2018-12-16 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planningBoard', '0002_funcionario_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='OportunidadeRecentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cod_projeto', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('SR', 'Serviço'), ('PJ', 'Projeto')], default='Serviço', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='OrdensDeServico',
            fields=[
                ('numero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='piac.OportunidadeRecentes')),
                ('jsa_status', models.BooleanField(default=False)),
                ('crol_status', models.BooleanField(default=False)),
                ('rels_status', models.BooleanField(default=False)),
                ('reld_status', models.BooleanField(default=False)),
                ('gpg_status', models.BooleanField(default=False)),
                ('mobile_status', models.BooleanField(default=False)),
                ('recursos', models.ManyToManyField(to='planningBoard.Funcionario')),
            ],
        ),
    ]
