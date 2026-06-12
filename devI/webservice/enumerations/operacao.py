from django.db import models

class Operacao(models.TextChoices):
    
    CELCIUS = "+", "Adição"
    SUBTRACAO = "-", "Subtração"
    MULTIPLICACAO = "*", "Multiplicação"
    DIVISAO= "/", "Divisão"
