from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from webservice.serializers import FreteSerializer
class Fretes(APIView):

    def get(self, request):
        
        dados = FreteSerializer()
        return Response(dados.data)
    
    def post(self, request):

        pass