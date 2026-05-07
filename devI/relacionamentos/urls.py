from django.urls import path
from .views import *
app_name = 'relacionamentos'

urlpatterns = [

    path('person/funcao/read/<int:id>', person.read, name='funcao_person_read'),
    path('person/funcao/list',person.list, name='funcao_person_list'),
    path('course/funcao/read/<int:id>', course.read, name='funcao_course_read'),
    path('person/funcao/create/', person.create, name='funcao_person_create'),
    path('person/funcao/update/<int:id>', person.update, name='funcao_person_update'),
    path('course/funcao/list',course.list, name='funcao_course_list'),
    path('person/funcao/gerar_cpf/<int:id>/',person.generate_cpf,name='funcao_person_generate_cpf'),
    path('person/funcao/delete/<int:id>',person.delete,name='funcao_person_delete')
]   