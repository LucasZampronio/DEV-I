from rest_framework import viewsets
from webservice.serializers.reporter import ReporterSerializer
from relacionamentos.models.reporter import Reporter
from webservice.views.base_security import BaseSecurity

class ReporterService(BaseSecurity ,viewsets.ModelViewSet):

    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer