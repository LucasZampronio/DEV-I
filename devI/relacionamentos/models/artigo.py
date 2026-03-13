from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date
from .base_model import BaseModel
from django.core.exceptions import ValidationError  # Adicione esta linha
from .reporter import Reporter
from django.contrib import admin  # Adicione esta linha para importar admin

class Artigo(BaseModel):
    titulo = models.CharField(max_length=100, validators=[MinLengthValidator(5)], verbose_name='Título do Artigo', help_text='Insira o título do artigo')

    publicacao = models.DateField(verbose_name='Data de Publicação', help_text='Insira a data de publicação do artigo', validators=[MinValueValidator(date.today)])

    autor = models.ForeignKey(Reporter, on_delete=models.CASCADE, help_text='Selecione o autor do artigo', verbose_name='Autor do Artigo')

    def __str__(self):
        return self.titulo
    
    def clean(self):
        data_publicacao = self.publicacao
        data_publicacao = data_publicacao.replace(year=data_publicacao.year - 18)  # Subtrai 18 anos da data de publicação para verificar a idade do autor
        if self.autor.data_nascimento > data_publicacao:
            raise ValidationError({'publicacao': 'Reporter não possui idade mínima para publicar.'})
        

    def __str__(self):
        return self.titulo
    
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao', 'autor')
    search_fields = ('titulo', 'autor__nome')  # Permite buscar por título e nome do autor
    list_filter = ('publicacao',)  # Permite filtrar por data de publicação