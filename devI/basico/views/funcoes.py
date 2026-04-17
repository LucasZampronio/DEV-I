from django.http import HttpResponse
from datetime import *


def funcao_primeira(request):
    mensagem = 'Hello World!'
    return HttpResponse(mensagem)


def funcao_saudacao(request):
    agora = datetime.now()
    mensagem = 'Boa noite!'
    if 6 <= agora.hour<12:
        mensagem = 'Bom dia'
    elif 12 <= agora.hour <18:
        mensagem = 'Boa tarde'
    elif 18<= agora.hour<24:
        mensagem = 'Boa noite'
    else:
        mensagem = 'Boa madrugada'

    saida = (f'<html><body><h1>{mensagem.upper()}</h1>'
             f'<br/>{agora}'
             f'<br/>{request.META['REMOTE_ADDR']}</body></html>')
    return HttpResponse(saida,status=200)

def funcao_saudacao_nome(request,nome):

    mensagem = f'Olá{nome.title()}'

    return HttpResponse(mensagem,status=200)

def funcao_alterar_senha(request,palavra):
    palavraAlterada = []
    for letra in palavra:
        if  letra.upper() == 'A':
            letra = '4'
            palavraAlterada.append(letra)
        elif letra.upper() == 'E':
            letra = '3' 
            palavraAlterada.append(letra)
        elif letra.upper() == 'I':
            letra = '1'
            palavraAlterada.append(letra)
        elif letra.upper() == 'O':
            letra = '0'
            palavraAlterada.append(letra)
        elif letra.upper() == 'U':
            letra = 'V'
            palavraAlterada.append(letra)
        else:
            palavraAlterada.append(letra)

    senha= ''.join(palavraAlterada)

    mensagem = (f'<html><body><h1>Parabens! você alterou sua senha</h1>'
                f'<br/>Senha antiga: {palavra}'
                f'<br/>Senha atual: {senha}</body></html>')

    return HttpResponse(mensagem, status=200)

def funcao_operacao(request,operacao,valor1,valor2):

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