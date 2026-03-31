from relacionamentos.enumerations import *
from relacionamentos.models.Cidade_csv import Cidade
from relacionamentos.models.Esporte_csv import Esporte
from relacionamentos.models.Time_csv import Time
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from .base_model import BaseModel

class Pessoaa(BaseModel):
    nome = models.CharField(max_length=40, validators=[MinLengthValidator(2)], verbose_name='Nome Completo', help_text='Insira o nome completo da pessoa')
    sexo = models.CharField(max_length=1, validators=[MinLengthValidator(1)],choices=Sexo , help_text='Insira o sexo da pessoa (M/F)')
    idade = models.IntegerField(verbose_name='Idade', help_text='Insira a idade da pessoa',validators=[MinValueValidator(0), MaxValueValidator(100)])
    renda = models.DecimalField(max_digits=10 , decimal_places=2, verbose_name='Renda', help_text='Insira a renda da pessoa')

    time_torce = models.ForeignKey(Time, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Time de Futebol', help_text='Selecione o time de futebol favorito da pessoa')
    esporte_praticado = models.ForeignKey(Esporte, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Esporte Praticado', help_text='Selecione o esporte praticado pela pessoa')
    cidade_residencia = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cidade de Residência', help_text='Selecione a cidade de residência da pessoa')


    def __str__(self):
        return self.nome