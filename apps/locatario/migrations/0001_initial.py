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
            name='Locatario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('data_nasc', models.DateField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_locatario', to='autenticacao.Perfil')),
            ],
            options={
                'verbose_name': 'Locatário',
                'verbose_name_plural': 'Locatários',
                'db_table': 'locatario',
            },
        ),
    ]
