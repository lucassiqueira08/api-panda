from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.autenticacao.api.serializers import PerfilSerializer
from apps.autenticacao.models import User, Perfil
from apps.locador.models import Locador


class LocadorSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    cnpj = serializers.RegexField(
        regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})",
        required=True,
        max_length=14,
        min_length=14,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=Locador.objects.all()),
            RegexValidator(
                regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
        ]
    )

    class Meta:
        model = Locador
        fields = (
            'id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
            'perfil')

    def create(self, validated_data):
        payload = {
            'nome_fantasia': validated_data.get('nome_fantasia', None),
            'razao_social': validated_data.get('razao_social', None),
            'inscricao_estadual': validated_data.get('inscricao_estadual', None),
            'cnpj': validated_data.get('cnpj'),
            'endereco': validated_data.get('endereco', None),
            'telefone': validated_data.get('telefone', None),
            'perfil': validated_data.get('perfil'),
            'usuario': validated_data['perfil']['usuario']
        }

        user = User.objects.create_user(payload['usuario']['username'], payload['usuario']['email'],
                                        payload['usuario']['password'])
        perfil = Perfil.objects.create(usuario=user)
        locador = Locador.objects.create(nome_fantasia=payload['nome_fantasia'],
                                         razao_social=payload['razao_social'],
                                         inscricao_estadual=payload['inscricao_estadual'], cnpj=payload['cnpj'],
                                         endereco=payload['endereco'],
                                         telefone=payload['telefone'], perfil=perfil)

        return locador


class LocadorSerializerSoft(serializers.ModelSerializer):
    cnpj = serializers.RegexField(
        regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})",
        required=True,
        max_length=14,
        min_length=14,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=Locador.objects.all()),
            RegexValidator(
                regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
        ]
    )

    class Meta:
        model = Locador
        fields = ('id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
                  'perfil')
