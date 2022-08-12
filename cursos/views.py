from rest_framework.generics import get_object_or_404
from rest_framework import generics

from rest_framework import viewsets  # API V2
from rest_framework.decorators import action #API V2
from rest_framework.response import Response #API V2
from rest_framework import mixins

from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import EhSuperUser


"""
API V1
"""

class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self): #sobrescrevendo método
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self): #sobrescrevendo método
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))

"""
API V2
"""

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser, 
        permissions.DjangoModelPermissions,
        )
    # EhSuperUser => classe criada no arquivo permissions.py
    # DjangoModelPermissions => permissão local para essa view com DjangoModelPermissions /definidas no admin
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None): #criando rota para trazer avaliações de um curso
        #implementação necessária/ não coberto pela paginção global no settings
        self.pagination_class.page_size = 2 
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)


        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response (serializer.data)
        

"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

class AvaliacaoViewSet(
    mixins.ListModelMixin,   
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,  
    viewsets.GenericViewSet
    ):
    """
    Forma selecionar recursos dos mixins para disponibilizar nas views da API
    """

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer