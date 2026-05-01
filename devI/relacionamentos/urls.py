from django.urls import path
from .views import *
app_name = 'relacionamentos'

urlpatterns = [

    path('person/funcao/read/<int:id>', person.read, name='funcao_person_read'),
    path('person/funcao/list',person.list, name='funcao_person_list'),
    path('course/funcao/read/<int:id>', course.read, name='funcao_course_read'),
    path('course/funcao/list',course.list, name='funcao_course_list'),

]   