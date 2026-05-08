from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Reporter
from ..forms.reporter import ReporterForm
import random
class ReporterListView(View):
    @staticmethod
    def get(request):
        reporteres = Reporter.objects.all()
        contexto = {
            "reporteres": reporteres
        }

        return render(request, 'reporter/list.html', contexto)
    
class ReporterReadView(View):
    @staticmethod
    def get(request, id):
        reporter = get_object_or_404(Reporter, pk=id)
        contexto = {
            "reporter": reporter
        }
        return render(request, 'reporter/read.html', contexto)

class ReporterCreateView(View):
    @staticmethod
    def get(request):
        form = ReporterForm()
        contexto = {
            "formulario": form
        }
        return render(request, "reporter/create.html",contexto)
    
    @staticmethod
    def post(request):
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:classe_reporter_list')
        else:
            contexto = {
                "formulario": form
            }
            return render(request, "reporter/create.html",contexto)



class ReporterDeleteView(View):
    @staticmethod
    def get(request, id):
        reporter = get_object_or_404(Reporter, pk=id)
        contexto = {
            "reporter": reporter
        }
        return render(request, 'reporter/delete.html', contexto)
    
    @staticmethod
    def post(request, id):
        reporter = get_object_or_404(Reporter, pk=id)
        try:
            confirmacao_reporter_id = request.POST.get('reporter_id')
            if int(confirmacao_reporter_id) == id:
                reporter.delete()
                return redirect('relacionamentos:classe_reporter_list')
        
        except Exception as ex:
            #TODO EXIBIR A MENSAGEM DE ERRO
            contexto = {}
            print(ex)
            return render(request,'reporter/list.html',contexto)    

class ReporterGenerateCpfView(View):
    @staticmethod
    def get(request, id):
        reporter = get_object_or_404(Reporter, pk=id)
        try:
            digits ='0123456789'
            reporter.cpf = ''.join(random.choice(digits) for i in range(11))
            reporter.save()
            return redirect('relacionamentos:classe_reporter_list')
        except Exception as e:
            print(f'Erro ao alterar cpf {reporter.id}')
            print(e)
            return redirect('relacionamentos:classe_reporter_list')
        
class ReporterUpdateView(View):
    @staticmethod
    def get(request, id):
        reporter = get_object_or_404(Reporter, pk=id)
        form = ReporterForm(instance=reporter)
        contexto = {
            "formulario": form,
            "reporter": reporter
        }
        return render(request, "reporter/update.html",contexto)
    
    @staticmethod
    def post(request, id):
        reporter = get_object_or_404(Reporter, pk=id)
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:classe_reporter_list')
        else:
            contexto = {
                "formulario": form,
                "reporter": reporter
            }
            return render(request, "reporter/update.html",contexto)