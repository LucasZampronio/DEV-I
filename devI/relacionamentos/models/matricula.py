from django.db import models
from .base_model import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from ..enumerations.status import Status
from .aluno import Aluno
from .disciplina import Disciplina
from django.core.exceptions import ValidationError

class Matricula(BaseModel):
    data_matricula = models.DateField(
        verbose_name='Data de Matrícula',
        help_text='Digite a data de matrícula do aluno',
    )

    nota = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        verbose_name='Nota',
        help_text='Digite a nota do aluno na disciplina',
    )

    frequencia = models.FloatField(
        verbose_name='Frequência',
        help_text='Digite a frequência do aluno na disciplina',
    )

    status = models.CharField(
        max_length=20,
        help_text='Digite o status da matrícula do aluno na disciplina',
        default=Status.MATRICULADO,
        choices=Status
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, help_text='Selecione o aluno para a matrícula')

    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, help_text='Selecione a disciplina para a matrícula')

    def __str__(self):
        return f'Matrícula de {self.aluno.nome} na disciplina {self.disciplina.nome}'
    
    def clean(self):
        if self.nota <= 7.0 and self.status == Status.APROVADO:
            raise ValidationError({'nota': 'A nota deve ser maior que 7.0 para aprovação.'})
        if self.nota > 7.0 and self.status == Status.REPROVADO:
            raise ValidationError({'nota': 'A nota deve ser menor ou igual a 7.0 para reprovação.'})
        if self.frequencia < 75.0 and self.status == Status.APROVADO:
            raise ValidationError({'frequencia': 'A frequência deve ser maior ou igual a 75% para aprovação.'})
        if self.frequencia >= 75.0 and self.status == Status.REPROVADO:
            raise ValidationError({'frequencia': 'A frequência deve ser menor que 75% para reprovação.'})