from django.views import View
from django.http import HttpResponse
class Primeira(View):

    @staticmethod
    def get(request):

        mensagem = 'Hello World!'
        return HttpResponse(mensagem)


class Saudacao(View):

    @staticmethod
    def get(request,nome):

        mensagem = f'Olá{nome.title()}'

        return HttpResponse(mensagem,status=200)
    
class SaudacaoNome(View):

    @staticmethod
    def get(operacao,valor1,valor2):
        
        mensagem = (f'<html><body><h1>ERROUUU</h1></body></html>')

        urls = ['adicao','subtracao','multiplicacao','divisao','resto','divisao_inteira']

        if operacao not in urls:
            return HttpResponse(mensagem,status=400)
        
        total = 0

        if operacao.lower() == 'adicao':
            total = valor1+valor2
        elif operacao.lower() == 'subtracao':
            total = valor1-valor2
        elif operacao.lower() == 'multiplicacao':
            total = valor1 * valor2
        elif operacao.lower() == 'divisao':
            total = valor1 / valor2
        elif operacao.lower() == 'resto':
            total = valor1 * valor2
        elif operacao.lower() == 'divisao_inteira':
            total = valor1 // valor2
        
        int(total)
        

        mensagem = (f'<html><body><h1>Operacão:</h1>'
                    f'<br/>Valor 1: {valor1}'
                    f'<br/>Valor 2: {valor2}'
                    f'<br/>Total : {total}</body></html>')


        return HttpResponse(mensagem,status=200)
            

