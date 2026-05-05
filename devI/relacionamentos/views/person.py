from ..models import Pessoa
from django.shortcuts import render,get_object_or_404, redirect
import random

def read(request, id):
    person = Pessoa.objects.get(id=id)
    contexto = {
        "pessoa": person
    }
    return render(request,'person/read.html',contexto)      

def list(request):
    people = Pessoa.objects.all()
    contexto = {
        "pessoas": people,
    } 
    return render(request,'person/list.html',contexto) 

def generate_cpf(request,id):
    person = get_object_or_404(Pessoa, pk=id)
    try:
        digits ='0123456789'
        person.cpf = ''.join(random.choice(digits) for i in range(11))
        person.save()
        return redirect('relacionamentos:funcao_person_list')
    except Exception as e:
        print(f'Erro ao alterar cpf {person.id}')
        print(e)
        return redirect('relacionamentos:funcao_person_list')
    
def delete(request,id):
    person = get_object_or_404(Pessoa,id=id)
    try:
        if request.method == 'POST':
            confirmacao_person_id = request.POST.get('pessoa_id')
            if int(confirmacao_person_id) == id:
                person.delete()
                return redirect('relacionamentos:funcao_person_list')
            raise ValueError(f'ID de confirmação e deleção não confere')
        
        else:
            contexto = {
                'pessoa' : person
            }
            return render(request,'person/delete.html',contexto)
    except Exception as ex:
        #TODO EXIBIR A MENSAGEM DE ERRO
        contexto = {}
        print(ex)
        return render(request,'person/list.html',contexto)