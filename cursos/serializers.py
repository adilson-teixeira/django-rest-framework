from rest_framework import serializers
from django.db.models import Avg, Sum
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta: 
        extra_kwargs = {
            'email': {'write_only': True}
        } # write_only (escrever)= o campo email não é apresentado quando alguém consultar.// apenas no cadasrtro
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    def validate_avaliacao(self, valor): #validação de campos
        """nome da função deve ser = validade_(nome do campo a ser validado)"""
        if  valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser no máximo 5.0')


class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship = retorna todas as avaliação dos cursos
    # Pode sobrecarregar o sistema se houver muitos dados para retornar
    # Ideal para poucos retornos como por ex: curso / autor;; em um curso há poucos autores
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True) #read_only apenas leitura

    """
    # HyperLinked Reated Field
    avaliacoes = serializers.HyperlinkedIdentityField(
        many=True, 
        read_only=True, 
        view_name='avaliacao-detail' # será criada uma rota (link) para detalhes
        #  "http:// ......../api/v2/avaliacoes/1/",
        #  "http:// ......../api/v2/avaliacoes/2/",
        #  "http:// ......../api/v2/avaliacoes/3/",
    )"""

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # retorna apenas o id das avaliações e o link deverá ser implementado pelo consumidor da api


    media_avaliacoes = serializers.SerializerMethodField()
    soma_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
            'soma_avaliacoes'
        )

    def get_media_avaliacoes(self, obj): #nome da função inicia com get_( nome do campo)
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        #return round(media * 2) / 2 #round (arredontamento para inteiro ou meio)
        return media

    def get_soma_avaliacoes(self, obj):
        soma = obj.avaliacoes.aggregate(Sum('avaliacao')).get('avaliacao__sum')

        if soma is None:
            return 0
        return soma

# No curso de django foi estudado em SIGNALS como inserir as funções de agregação diretamente em campos de banco de dados.