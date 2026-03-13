from .base_model import *
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from relacionamentos.validators.validacao_cpf import validacao_cpf
from datetime import date

class Pessoa(BaseModel):
    nome = models.CharField(max_length=100
                            , verbose_name='Nome'
                            , help_text='Insira o nome da pessoa'
                            , validators=[MinLengthValidator(5)])

    data_nascimento = models.DateField(verbose_name='Data de Nascimento'
                                      , help_text='Insira a data de nascimento da pessoa')
    cpf = models.CharField(max_length=11, unique=True
                           , validators=[MinLengthValidator(11), validacao_cpf]
                           , help_text='Insira o CPF da pessoa'
                           , verbose_name='CPF')
    
    def clean(self):
        hoje = date.today()
        if self.data_nascimento > hoje:
            raise ValidationError({'data_nascimento': 'A data de nascimento não pode ser no futuro.'})
    
    def __str__(self):
        return self.nome