from .base_model import BaseModel
from .pessoa import Pessoa
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from datetime import date

class Passaporte(BaseModel):
    numero = models.CharField(max_length=20, unique=True,
                              validators=[MinLengthValidator(4)],
                              help_text='Número do passaporte',
                              verbose_name='Numero do Passaporte')
    
    emissao = models.DateField(verbose_name='Data de Emissao',
                               help_text='Data de emissão do passaporte',
                               validators=[MinValueValidator(date.today)])
    
    vencimento = models.DateField(verbose_name='Data de Vencimento',
                                help_text='Data de vencimento do passaporte')
    
    pessoa = models.OneToOneField(Pessoa, help_text='Pessoa associada ao passaporte', on_delete=models.CASCADE)

    def clean(self):
        if self.vencimento <= self.emissao:
            raise ValidationError({'vencimento': 'A data de vencimento deve ser posterior à data de emissão.', 'emissao': 'A data de emissão deve ser anterior à data de vencimento.'})
        
        if self.pessoa.data_nascimento > self.emissao:
            raise ValidationError({'emissao': 'A data de emissão do passaporte não pode ser anterior à data de nascimento da pessoa.'})
        
    def __str__(self):
        return f'Passaporte {self.numero} - {self.pessoa.nome}'