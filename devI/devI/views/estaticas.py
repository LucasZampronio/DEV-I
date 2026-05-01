from django.views import View
from django.shortcuts  import render


class IndexView(View):
    @staticmethod   
    def get(request):
        contexto={
            "mensagem" : "Bem-vindo a aula de DevI"
        }
        return render(request, "index.html",contexto)