from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from relacionamentos.models.passaporte import Passaporte
from webservice.serializers.passaporte import PassaporteSerializer
from webservice.views.base_security import BaseSecurity

class PassaporteServiceList(BaseSecurity, ListAPIView, CreateAPIView):
    queryset = Passaporte.objects.all()
    serializer_class = PassaporteSerializer

class PassaporteService(BaseSecurity, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ):
    queryset = Passaporte.objects.all()
    serializer_class = PassaporteSerializer
    lookup_field = "numero"
    