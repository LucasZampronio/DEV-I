from django.db import models
class Regiao(models.TextChoices):
    Norte = 'N','Norte'
    Sul = 'S', 'Sul'
    Sudeste = 'SE', 'Sudeste'
    Centrooeste = 'CO', 'Centrooeste'
    Nordeste = 'NE', 'Nordeste'
