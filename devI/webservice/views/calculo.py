from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import CalculoSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
class Calculo(APIView):
    def get(self,request):
        dados = CalculoSerializer()
        return Response(dados.data)
    
    def post(self,request):
        try:
            dados_requisicao = JSONParser().parse(request)
            dados = CalculoSerializer(data=dados_requisicao)

            if dados.is_valid():
                dados.calcular()
                return Response(dados.data)
            else:
                return Response(dados.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            contexto = {
                "erro": str(e)
            }
            return Response(contexto, status=status.HTTP_401_UNAUTHORIZED)