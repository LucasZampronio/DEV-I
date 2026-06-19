from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request):
    enderecos = {
        "saudacao_funcao": reverse("webservice:saudacao_funcao", request=request),
        "saudacao_classe": reverse("webservice:saudacao_classe", request=request),
    }
    return Response(enderecos)
