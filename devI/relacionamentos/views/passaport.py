from django.views.generic import ListView, DetailView, DeleteView, CreateView,UpdateView
from ..models.passaporte import Passaporte
from ..forms.passaport import PassaporteForm
from django.urls import reverse_lazy

class PassaporteListGenericView(ListView):
    model = Passaporte
    queryset = Passaporte.objects.all()
    context_object_name = "passaportes"
    template_name = "passaport/list.html"

class PassaporteReadGenericView(DetailView):
    model = Passaporte
    fields = "__all__"
    queryset = Passaporte.objects.all()
    context_object_name = 'passaporte'
    template_name = 'passaport/read.html'
    success_url = reverse_lazy('relacionamentos:classe_generica_passaporte_list')

class PassaporteDeleteGenericView(DeleteView):
    model = Passaporte
    context_object_name = 'passaporte'
    template_name = 'passaport/delete.html'
    success_url = reverse_lazy('relacionamentos:classe_generica_passaporte_list')

class PassaporteCreateGenericView(CreateView):
    model = Passaporte
    form_class = PassaporteForm
    context_object_name = 'passaporte'
    template_name = 'passaport/create.html'
    success_url = reverse_lazy('relacionamentos:classe_generica_passaporte_list')

class PassaporteUpdateGenericView(UpdateView):
    model = Passaporte
    form_class = PassaporteForm
    context_object_name = 'passaporte'
    template_name = 'passaport/update.html'
    success_url = reverse_lazy('relacionamentos:classe_generica_passaporte_list')