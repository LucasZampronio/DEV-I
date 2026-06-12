from rest_framework import serializers
from webservice.enumerations import Operacao

class CalculoSerializer(serializers.Serializer):

    primeiro_termo = serializers.FloatField(required=True)
    segundo_termo = serializers.FloatField(required=True)
    operacao = serializers.ChoiceField(required=True, choices=Operacao)
    resultado = serializers.CharField(required=False)

    class Meta:
        fields = ['primeiro_termo','segundo_termo','operacao']

    def calcular(self):

        primeiro_valor = self.validated_data.get("primeiro_termo")
        segundo_valor = self.validated_data.get("segundo_termo")
        op = self.validated_data.get("operacao")

        match op:
            case Operacao.ADICAO:
                self.validated_data.update({"resultado": primeiro_valor + segundo_valor})
                self.validated_data.update({"operacao": Operacao.ADICAO.label})

            case Operacao.SUBTRACAO:
                self.validated_data.update({"resultado": primeiro_valor - segundo_valor})
                self.validated_data.update({"operacao": Operacao.SUBTRACAO.label})

            case Operacao.MULTIPLICACAO:
                self.validated_data.update({"resultado": primeiro_valor * segundo_valor})
                self.validated_data.update({"operacao": Operacao.MULTIPLICACAO.label})

            case Operacao.DIVISAO:
                self.validated_data.update({"resultado": primeiro_valor / segundo_valor})
                self.validated_data.update({"operacao": Operacao.DIVISAO.label})

            case _:
                raise NotImplementedError("NotImplemented")