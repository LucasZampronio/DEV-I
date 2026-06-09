from django.urls import path
from webservice.views import saudacao, Saudacao
from webservice.views import api_root

app_name = 'webservice'

urlpatterns = [
    path('saudacao', saudacao, name='saudacao_funcao'),
    path('saudacao_classe', Saudacao.as_view, name='saudacao_classe'),
    path('',api_root,name='api_root')
]