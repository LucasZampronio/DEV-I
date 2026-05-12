from .base_form import BaseForm
from ..models.passaporte import Passaporte


class PassaportForm(BaseForm):
    class Meta:
        model = Passaporte
        fields = "__all__"
