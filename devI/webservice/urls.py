from django.urls import path
from webservice.views import saudacao, Saudacao
from webservice.views import api_root
from webservice.views import Calculo, Temperatura
from webservice.views import PessoaSimpleService, PersonService, ReporterService
from rest_framework.routers import DefaultRouter
from webservice.views.passaporte import PassaporteServiceList, PassaporteService
from rest_framework.authtoken.views import obtain_auth_token

app_name = "webservice"

router = DefaultRouter()

router.register(r"reporter", ReporterService, basename="reporter")

urlpatterns = [
    path("saudacao", saudacao, name="saudacao_funcao"),
    path("saudacao_classe", Saudacao.as_view(), name="saudacao_classe"),
    path("calculo", Calculo.as_view(), name="calculo"),
    path("temperatura", Temperatura.as_view(), name="temperatura"),
    path("pessoa", PessoaSimpleService.as_view(), name="pessoa_simples"),
    path("passaporte", PassaporteServiceList.as_view(), name="passaporte_list"),
    path("passaporte/<str:numero>", PassaporteService.as_view(), name="passaporte_update"),
    path("autenticar", obtain_auth_token),
    path("pessoa/<int:pk>", PersonService.as_view(), name="pessoa_object"),
    path("", api_root, name="api_root"),
]

urlpatterns.extend(router.urls)