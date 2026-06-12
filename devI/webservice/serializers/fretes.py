from rest_framework import serializers
from webservice.enumerations import Regioes

class FreteSerializer(serializers.Serializer):

    peso = serializers.FloatField(required=True)
    regiao_origem = serializers.ChoiceField(required=True,choices=Regioes)
    regiao_destino = serializers.ChoiceField(required=True,choices=Regioes)
    valor_base = serializers.FloatField(required=False)
    adicional_peso = serializers.FloatField(required=False)
    adicional_regiao =serializers.FloatField(required=False)
    valor_total= serializers.FloatField(required=False)