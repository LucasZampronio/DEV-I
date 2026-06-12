from rest_framework.views import APIView
from webservice.serializers import TemperaturaSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status


class Temperatura(APIView):

    def get(self, request):
        
        dados = TemperaturaSerializer()
        return Response(dados.data)
    
    def post(self, request):

        dados_req = JSONParser().parse(request)
        conversao = TemperaturaSerializer(data=dados_req)

        try:
            if conversao.is_valid():
                conversao.converter()
                return Response(conversao.data)
            
            else:
                return Response(conversao.errors,status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            contexto = {"erro": str(e)}

            return Response(contexto, status=status.HTTP_401_UNAUTHORIZED)