from .base_model import BaseModel
from django.db.models import CharField
from django.core.validators import MinLengthValidator

class Esporte(BaseModel):
    nome = CharField(max_length=20,validators=[MinLengthValidator(4)],verbose_name='Nome do Esporte',help_text='Insira o nome do esporte')

    def __str__(self): 
        return self.nome