from django.views.generic import ListView, DetailView, DeleteView, CreateView
from relacionamentos.models.passaporte import Passaporte
from relacionamentos.forms.passaport import PassaportForm
from django.urls import reverse_lazy

class PassportListGenericView(ListView):

    model = Passaporte
    queryset = Passaporte.objects.all()
    context_object_name = "passaportes"
    template_name = "passaport/list.html"

    # def get_queryset(self):

    #     Aqui definimos alguma consulta especializada para a página inicial
    #     return do tipo query_set

class PassportReadGenericView(DetailView):

    model = Passaporte
    template_name = "passaport/read.html"
    fields = "__all__"
    success_url = reverse_lazy("relacionamentos:classe_generica_passaporte_read")

class PassportDeleteGenericView(DeleteView):

    model = Passaporte
    template_name = "passaport/delete.html"
    success_url = reverse_lazy("relacionamentos:classe_generica_passaporte_list")

class PassportCreateGenericView(CreateView):

    model = Passaporte
    template_name = "passaport/create.html"
    success_url = reverse_lazy("relacionamentos:classe_generica_passaporte_list")
    form_class = PassaportForm