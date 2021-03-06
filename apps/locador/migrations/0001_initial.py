# Generated by Django 2.2 on 2019-04-20 01:58

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


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
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nome_fantasia', models.CharField(blank=True, max_length=100, null=True)),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=12, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_locador', to='autenticacao.Perfil')),
            ],
            options={
                'verbose_name': 'Locador',
                'verbose_name_plural': 'Locadores',
                'db_table': 'locador',
            },
        ),
    ]
