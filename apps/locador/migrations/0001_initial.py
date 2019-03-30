# Generated by Django 2.1.7 on 2019-03-30 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(blank=True, max_length=100, null=True)),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=12, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacao.Perfil')),
                ('plano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.Plano')),
            ],
            options={
                'verbose_name': 'Locador',
                'verbose_name_plural': 'Locadores',
                'db_table': 'locador',
            },
        ),
    ]
