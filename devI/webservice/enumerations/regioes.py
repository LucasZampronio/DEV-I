from django.db import models

class Regioes(models.TextChoices):

    SUL = "S", 'Sul'
    SUDESTE = "SD", "Suldeste"
    CENTRO_OESTE = "CO", "Centro Oeste"
    NORDESTE = "ND", "Nordeste"
    NORTE = "N", "Norte"