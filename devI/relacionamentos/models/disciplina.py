from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Disciplina(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome da Disciplina',
        help_text='Digite o nome da disciplina',
        validators=[MinLengthValidator(3)]
    )
    
    sigla = models.CharField(
        max_length=5,
        unique=True,
        validators=[MinLengthValidator(3)],
        help_text='Digite a sigla da disciplina',
        verbose_name='Sigla da Disciplina'
    )
    semestre = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Digite o semestre da disciplina',
        verbose_name='Semestre da Disciplina'
    )
    ementa = models.TextField(help_text='Digite a ementa da disciplina', verbose_name='Ementa da Disciplina')

    def __str__(self):
        return f'{self.nome} ({self.sigla}) - Semestre {self.semestre}' 