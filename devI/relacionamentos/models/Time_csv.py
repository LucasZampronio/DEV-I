from .base_model import BaseModel
from django.db.models import CharField
from django.core.validators import MinLengthValidator

class Time(BaseModel):
    nome = CharField(max_length=20,validators=[MinLengthValidator(3)],verbose_name='Nome do Time',help_text='Insira o nome do time')

    def __str__(self): 
        return self.nome