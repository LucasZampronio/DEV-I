from rest_framework import serializers
from ..enumerations import Regiao

class CalculoSerializer(serializers.Serializer):
    peso = serializers.FloatField(required=True)
    regiao_origem = serializers.FloatField(required=True,choices=Regiao)
    regiao_destino = serializers.ChoiceField(required=True,choices=Regiao)
    valor_base = serializers.CharField(required=False)
    adicional_peso = serializers.CharField(required=False)
    adicional_regiao = serializers.CharField(required=False)
    valor_total = serializers.CharField(required=False)

    class Meta:
        fields = ['peso','regiao_origem','regiao_destino','valor_base','adicional_peso','adicional_regiao','valor_total']

    def calcularFrete(self):
        peso_valor = self.validated_data.get('peso')
        regiao_origem_valor = self.validated_data.get('regiao_origem')
        regiao_destino_valor = self.validated_data.get('regiao_destino')
        valor_base_valor = self.validated_data.get('valor_base')
        adicional_peso_valor = self.validated_data.get('adicional_peso')
        adicional_regiao = self.validated_data.get('adicional_regiao')
        valor_total_valor = self.validated_data.get('valor_total')

        if regiao_destino_valor == regiao_origem_valor:
            valor_total_valor +=10
        elif regiao_destino_valor == Regiao.Sul.value or regiao_destino_valor == Regiao.Sudeste.value:
            valor_total_valor += 20
        elif regiao_destino_valor == Regiao.Norte.value or regiao_destino_valor == Regiao.Nordeste:
            valor_total_valor += 25
        elif regiao_destino_valor == Regiao.Centrooeste or regiao_destino_valor == Regiao.Sudeste:

        raise NotImplementedError('Operação Não Implementada')              
