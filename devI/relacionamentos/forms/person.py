from .baseForm import BaseForm
from relacionamentos.models import Pessoa

class PersonForm(BaseForm):
    class Meta:
        model = Pessoa
        fields = "__all__"