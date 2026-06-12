from django.urls import path
from webservice.views import saudacao, Saudacao, Calculo, Temperatura, Regioes
from webservice.views import api_root

app_name = 'webservice'

urlpatterns = [
    path('saudacao', saudacao, name='saudacao_funcao'),
    path('saudacao_classe', Saudacao.as_view(), name='saudacao_classe'),
    path('',api_root,name='api_root'),
    path('calcular', Calculo.as_view(),name='Calcular'),
    path('temperatura', Temperatura.as_view(),name='Temperatura'),
    path('frete', Regioes.as_view(),name='frete')
]