from rest_framework.views import APIView, Response
from relacionamentos.models import Pessoa
from webservice.serializers import (
    PersonMinimalSerializer,
    PersonCompleteSerializer,
    PersonService,
)
from django.shortcuts import get_object_or_404


class PessoaSimpleService(APIView):
    queryset = Pessoa.objects.all()
    serializer_class = PersonMinimalSerializer

    def get(self, request):
        pessoas = Pessoa.objects.all()
        contexto = {"request": request}

        serializador = PersonMinimalSerializer(pessoas, many=True, context=contexto)

        return Response(serializador.data)


class PersonService(APIView):

    serializer_clas = PersonCompleteSerializer
    queryser = Pessoa.objects.all()

    def get(self, request, pk):

        pessoa = get_object_or_404(Pessoa, pk=pk)
        contexto = {"request": request}

        serializador = PersonCompleteSerializer(pessoa, context=contexto)

        return Response(serializador.data)

    def delete(self, request, pk):

        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa.delete()

        return Response(status=204)

    def put(self, request, pk):

        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa_dados = request.data

        contexto = {"request": request}

        serializador = PersonCompleteSerializer(
            pessoa, data=pessoa_dados, context=contexto
        )

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)

        else:
            return Response(serializador.error, status=400)

    def post(self, request):

        pessoa_dados = request.data
        contexto = {"request": request}

        serializador = PersonCompleteSerializer(data=pessoa_dados, context=contexto)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=201)

        else:
            return Response(serializador.error, status=400)