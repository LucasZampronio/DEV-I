from django.db.models import Q
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from relacionamentos.models import Pessoa, Reporter


class BuscarView(View):

    @staticmethod
    def get(request):

        resultados = {}

        query = request.GET.get("query")

        pessoas = Pessoa.objects.filter(
            Q(nome__icontains=query) | (Q(cpf__icontains=query))
        )

        pessoas_urls = []

        for pessoa in pessoas:

            url = reverse_lazy("relacionamentos:funcao_person_read", kwargs={"id": pessoa.id})
            pessoas_urls.append((url, pessoa))

        reporters = Reporter.objects.filter(
            Q(nome__icontains=query) | (Q(cpf__icontains=query))
        )

        reporter_urls = []

        for reporter in reporters:

            url = reverse_lazy("relacionamentos:classe_reporter_read", kwargs={"id": reporter.id})
            reporter_urls.append((url, reporter))

        if len(reporter_urls) > 0 or len(pessoas_urls) > 0:
            resultados["Pessoas"] = pessoas_urls
            resultados["Reporters"] = reporter_urls
        else:
            resultados = None

        contexto = {"resultados": resultados, "query": query}

        return render(request, "buscar/resultado.html", contexto)
