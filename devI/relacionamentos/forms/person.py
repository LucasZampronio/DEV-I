from .base_form import BaseForm
from ..models.pessoa import Pessoa


class PersonForm(BaseForm):
    class Meta:
        model = Pessoa
        fields = "__all__"
