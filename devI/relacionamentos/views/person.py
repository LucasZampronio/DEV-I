from ..models import Pessoa
from django.shortcuts  import render


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