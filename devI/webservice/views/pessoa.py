from rest_framework.views import APIView, Response
from relacionamentos.models import Pessoa
from webservice.serializers import PersonMinimalSerializer


class PessoaSimpleService(APIView):
    queryset = Pessoa.objects.all()
    serializer_class = PersonMinimalSerializer

    def get(self,request):
        pessoas = Pessoa.objects.all()
        contexto = {'request': request}

        serializador = PersonMinimalSerializer(pessoas, many=True, context=contexto)

        return Response(serializador.data)