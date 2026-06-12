from django.db import models
class Operacao(models.TextChoices):
    ADICAO = '+','ADIÇÃO'
    SUBTRACAO = '-','SUBTRAÇÃO'
    MULTIPLICACAO = '*','MULTIPLICAÇÃO'
    DIVISAO = '/','DIVISÃO'
    AND = '&','E Lógico'
    OR = '|', 'OU Lógico'