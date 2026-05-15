from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from ..forms.contato import ContatoForm


class ContatoView(View):

    @staticmethod
    def get(request):
        formulario = ContatoForm()

        contexto = {"formulario": formulario, "form_url": "contato_classe"}

        return render(request, "contato/contato.html", contexto)

    @staticmethod
    def post(request):
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():

            assunto = formulario.cleaned_data.get("assunto")
            remetente = formulario.cleaned_data.get("remetente")
            mensagem = formulario.cleaned_data.get("mensagem")
            data = formulario.cleaned_data.get("data")
            copia = formulario.cleaned_data.get("copia")

            para = ["contato@restinga.ifrs.edu.br"]

            if copia:
                para.append(remetente)

            """
            send_mail(
                subject=assunto,
                message=mensagem,
                from_email=remetente,
                recipient_list=para,
            )
            """

            contexto = {"formulario": formulario, "destinatarios": para}

        return render(request, "contato/obrigado.html", contexto)
