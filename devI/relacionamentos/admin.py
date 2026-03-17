from django.contrib import admin
from .models import Pessoa  
from .models import Passaporte
from .models import Reporter
from .models import Artigo
from .models.artigo import ArtigoAdmin
from .models import Revista
from .models import Reportagem
from .models import Aluno
from .models import Disciplina  
from .models import Matricula

admin.site.register(Pessoa)
admin.site.register(Passaporte)
admin.site.register(Reporter)
admin.site.register(Revista)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Reportagem) 
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Matricula)