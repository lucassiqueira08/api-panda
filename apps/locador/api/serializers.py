from rest_framework import serializers, status
from rest_framework.response import Response

from apps.autenticacao.api.serializers import PerfilSerializer
from apps.autenticacao.models import Perfil
from apps.autenticacao.models import User
from apps.locador.models import Locador


class LocadorSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = Locador
        fields = (
            'id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
            'perfil')

    def create(self, validated_data):
        try:
            nome_fantasia = validated_data['nome_fantasia']
            razao_social = validated_data['razao_social']
            inscricao_estadual = validated_data['inscricao_estadual']
            cnpj = validated_data['cnpj']
            endereco = validated_data['endereco']
            telefone = validated_data['telefone']
            perfil = validated_data['perfil']

            usuario = perfil['usuario']

            user = User.objects.create_user(usuario['username'], usuario['email'], usuario['password'])
            perfil = Perfil.objects.create(usuario=user)
            locador = Locador.objects.create(nome_fantasia=nome_fantasia, razao_social=razao_social,
                                             inscricao_estadual=inscricao_estadual, cnpj=cnpj, endereco=endereco,
                                             telefone=telefone, perfil=perfil)

            return locador

        except Exception:
            return Response('Não foi possível efetuar o cadastro.', status.HTTP_400_BAD_REQUEST)


class LocadorSerializerSoft(serializers.ModelSerializer):
    class Meta:
        model = Locador
        fields = ('id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
                  'perfil')