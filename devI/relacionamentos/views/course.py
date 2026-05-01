from ..models import Matricula
from django.shortcuts  import render


def read(request, id):
    course = Matricula.objects.get(id=id)
    contexto = {
        "matricula": course
    }
    return render(request,'course/read.html',contexto)      

def list(request):
    course = Matricula.objects.all()
    contexto = {
        "matriculas": course,
    }
    return render(request,'course/list.html',contexto) 