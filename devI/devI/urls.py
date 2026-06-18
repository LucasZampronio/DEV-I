"""
URL configuration for devI project.


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from devI.views import IndexView
from .views.contato import ContatoView
from .views.buscar import BuscarView
from django.contrib.auth import views as auth_views

from .views.perfil import PerfilView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicial/", include("basico.urls", namespace="")),
    path("", IndexView.as_view(), name="index"),
    path(
        "relacionamentos/", include("relacionamentos.urls", namespace="relacionamentos")
    ),
    path('relacionamentos/ws/', include('webservice.urls')),
    path("contato/classe", ContatoView.as_view(), name="contato_classe"),
    path('buscar/classe/', BuscarView.as_view(), name='buscar'),

    # # É PRECISO CRIAR AS VIEWS ACIMA DA URL CONTAS, COMO O DJANGO JÁ POSSUI TODAS AS URLS RELACIONADAS À AUTENTICAÇÃO PRONTAS,
    
    path("contas/login/", auth_views.LoginView.as_view(
        template_name = "contas/login.html",
    )),

    path("contas/", include('django.contrib.auth.urls')),

    path("contas/perfil", PerfilView.as_view(), name='profile')
]
