from django.urls import path
from .views import *

app_name = "relacionamentos"

# URLS apontam para VIEWS

urlpatterns = [
    path("person/funcao/read/<int:id>", person.read, name="funcao_person_read"),
    path("person/funcao/list", person.list, name="funcao_person_list"),
    path("course/funcao/read/<int:id>", course.read, name="funcao_course_read"),
    path("course/funcao/list", course.list, name="funcao_course_list"),
    path(
        "person/funcao/gerar_cpf/<int:id>/",
        person.generate_cpf,
        name="funcao_person_generate_cpf",
    ),
    path("person/funcao/delete/<int:id>", person.delete, name="funcao_person_delete"),
    path("person/funcao/create", person.create, name="funcao_person_create"),
    path("person/funcao/update/<int:id>", person.update, name="funcao_person_update"),
    # reporteres
    path(
        "reporter/classe/list", ReporterListView.as_view(), name="classe_reporter_list"
    ),
    path(
        "reporter/classe/read/<int:id>",
        ReporterReadView.as_view(),
        name="classe_reporter_read",
    ),
    path(
        "reporter/classe/delete/<int:id>",
        ReporterDeleteView.as_view(),
        name="classe_reporter_delete",
    ),

    # passaporte

    # CLASSE GENÉRICA
    path("passaporte/classe_generica/list",PassportListGenericView.as_view(), name= "classe_generica_passaporte_list"),
    path("passaporte/classe_generica/create",PassportCreateGenericView.as_view(), name= "classe_generica_passaporte_create"),
    path("passaporte/classe_generica/read/<int:pk>",PassportReadGenericView.as_view(), name= "classe_generica_passaporte_read"),
    path("passaporte/classe_generica/delete/<int:pk>",PassportDeleteGenericView.as_view(), name= "classe_generica_passaporte_delete"),
    
]
