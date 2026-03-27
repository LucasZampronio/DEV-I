from django.db import models
from django.core.validators import MinLengthValidator
from .base_model import BaseModel

class Cidade(BaseModel):
    nome = models.CharField(max_length=100,validators=[MinLengthValidator(2)], verbose_name='Nome da Cidade', help_text='Insira o nome da cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado',validators=[MinLengthValidator(2)], help_text='Insira a sigla do estado')

    def __str__(self):
        return f'{self.nome} - {self.estado}'