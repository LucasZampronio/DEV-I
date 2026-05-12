from .baseForm import BaseForm
from relacionamentos.models import Passaporte

class PassaporteForm(BaseForm):
    class Meta:
        model = Passaporte
        fields = "__all__"