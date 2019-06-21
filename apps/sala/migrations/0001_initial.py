# Generated by Django 2.2.2 on 2019-06-20 23:51

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('figura_url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tipo de Recurso',
                'verbose_name_plural': 'Tipos de Recursos',
                'db_table': 'tipo_recurso',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('metragem', models.FloatField(blank=True, null=True)),
                ('capacidade', models.IntegerField()),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('cep', models.CharField(max_length=20)),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
                ('locador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locador_sala', to='locador.Locador')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'db_table': 'sala',
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sala_recurso', to='sala.Sala')),
                ('tipo_recurso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tipo_recurso_recurso', to='sala.TipoRecurso')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
                'db_table': 'recurso',
            },
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(max_length=200)),
                ('principal', models.BooleanField(default=False)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foto_sala', to='sala.Sala')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galeria',
                'db_table': 'galeria',
            },
        ),
    ]
