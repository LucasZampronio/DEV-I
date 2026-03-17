from django.db import models

class Status(models.TextChoices):
    APROVADO = 'Aprovado', 'Aprovado'
    REPROVADO = 'Reprovado', 'Reprovado'
    MATRICULADO = 'Matriculado', 'Matriculado'
    TRANCADO = 'Trancado', 'Trancado'
    EM_EXAME = 'Em Exame', 'Em Exame'
    APROVADO_EM_EXAME = 'Aprovado em Exame', 'Aprovado em Exame'