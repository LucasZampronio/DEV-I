from django.db import models
from django.core.validators import MinLengthValidator
from .pessoa import Pessoa

class Reporter(Pessoa):

    email = models.EmailField(unique=True, max_length=100
                              ,verbose_name='Email do Repórter'
                              ,help_text='Insira o institucional'
                              ,validators=[MinLengthValidator(5)])
    
