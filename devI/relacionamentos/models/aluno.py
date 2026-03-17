from .pessoa import Pessoa
from django.db import models
from django.core.validators import MinLengthValidator
from .disciplina import Disciplina


class Aluno(Pessoa):
    email = models.EmailField(
        verbose_name='E-mail',
        help_text='E-mail institucional do aluno',
        unique=True,
        max_length=254,
    )

    cod = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        unique=True,
        verbose_name='Matricula',
        help_text='Digite a matricula do aluno',
    )

    disciplinas = models.ManyToManyField(Disciplina,through='Matricula',through_fields=('aluno','disciplina'),help_text='Selecione as disciplinas do aluno')