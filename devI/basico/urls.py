from django.urls import path
import basico.views.funcoes as views
from basico.views import Primeira, Saudacao, SaudacaoNome
app_name = 'basico'

urlpatterns = [

    path('funcao/primeira', views.funcao_primeira, name='funcao_primeira'),
    path('funcao/saudacao', views.funcao_saudacao, name='saudacao'),
    path('funcao/saudacao_nome/<str:nome>', views.funcao_saudacao_nome, name='saudacao_nome'),
    path('funcao/alterar_senha/<str:palavra>', views.funcao_alterar_senha, name='alterar_senha'),
    path('funcao/<str:operacao>/<int:valor1>/<int:valor2>', views.funcao_operacao, name='funcao_operacao'),
    path('classe/primeira', Primeira.as_view(), name='classe_primeira'),
    path('classe/saudacao', Saudacao.as_view(), name='Classe_saudacao'),
    path('classe/saudacao_nome/<str:nome>', SaudacaoNome.as_view(), name='Classe_saudacao_nome')

]