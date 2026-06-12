from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# ws usando funcoes
@api_view(['GET'])
def saudacao(request):
    resposta = {
        "mensagem" : "Boa Noite"
    }
    return Response(resposta) 

# ws usando classes

class Saudacao(APIView):
    def get(self, request):
        resposta = {
            'mensagem': 'Boa noite, sou a resposta da classe!'
        }
        return Response(resposta)