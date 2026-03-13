from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date

from .base_model import BaseModel
from .revista import Revista

class Reportagem(BaseModel):
    titulo = models.CharField(max_length=200,
                              validators=[MinLengthValidator(3)],
                              verbose_name='Título da Reportagem',
                              help_text='Insira o título da reportagem')

    publicacao = models.DateField(verbose_name='Data de Publicação',
                                  help_text='Insira a data de publicação da reportagem',
                                  validators=[MinValueValidator(date.today)])
    
    revistas = models.ManyToManyField(Revista, help_text='Revistas associadas à reportagem')