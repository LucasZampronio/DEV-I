from django.views import View
from ..models.reporter import Reporter
from django.shortcuts import render, redirect, get_object_or_404


class ReporterListView(View):

    @staticmethod
    def get(request):
        reporteres = Reporter.objects.all()
        contexto = {
            "reporteres": reporteres,
        }

        return render(request, "reporter/list.html", contexto)


class ReporterReadView(View):

    @staticmethod
    def get(request, id):
        reporter = get_object_or_404(Reporter, id=id)
        contexto = {"reporter": reporter}

        return render(request, "reporter/read.html", contexto)


class ReporterDeleteView(View):

    @staticmethod
    def get(request, id):
        reporter = get_object_or_404(Reporter, id=id)

        try:
            contexto = {"reporter": reporter}
            return render(request, "reporter/delete.html", contexto)

        except Exception as e:
            contexto = {"error": "Ocorreu um erro ao tentar deletar o reporter."}

            print(str(e))
            return render(request, "reporter/list.html", contexto)

    @staticmethod
    def post(request, id):
        reporter = get_object_or_404(Reporter, id=id)

        try:
            reporter_id_form = request.POST.get("reporter_id")
            if int(reporter_id_form) == id:
                reporter.delete()
                return redirect("relacionamentos:classe_reporter_list")
            
        except Exception as e:
            print(str(e))
            contexto = {"error": "Ocorreu um erro ao tentar deletar o reporter."}
            return render(request, "reporter/list.html", contexto)
