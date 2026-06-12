from rest_framework import serializers
from ..enumerations import Temperatura

class TemperaturaSerializer(serializers.Serializer):
    primeira_temperatura = serializers.ChoiceField(required=True,choices=Temperatura)
    segunda_temperatura = serializers.ChoiceField(required=True,choices=Temperatura)
    valor = serializers.FloatField(required=True)
    resultado_conversao = serializers.CharField(required=False)

    class Meta:
        fields = ['primeira_temperatura','segunda_temperatura','valor','resultado_conversao']

    def calcularTemperatura(self):
        primeiro = self.validated_data.get('primeira_temperatura')
        segundo = self.validated_data.get('segunda_temperatura')
        valortemperatura = self.validated_data.get('valor')

        if segundo == Temperatura.Kelvin.value:
            if primeiro == Temperatura.Fahrenheit.value:
                valortemperatura = (valortemperatura - 273.15) * 9/5 + 32
                self.validated_data.update({'resultado_conversao': valortemperatura})
                self._validated_data.update({'Temperatura': Temperatura.Fahrenheit.label})
            else:
                valortemperatura -= 273.15
                self.validated_data.update({'resultado_conversao': valortemperatura})
                self._validated_data.update({'Temperatura': Temperatura.Celcius.label})

        if segundo == Temperatura.Fahrenheit.value:
            if primeiro == Temperatura.Celcius.value:
                valortemperatura = (valortemperatura - 32) * 5/9
                self.validated_data.update({'resultado_conversao': valortemperatura})
                self._validated_data.update({'Temperatura': Temperatura.Celcius.label})
            else:
                valortemperatura = (valortemperatura - 32) * 5/9 + 273.15
                self.validated_data.update({'resultado_conversao': valortemperatura})
                self._validated_data.update({'Temperatura': Temperatura.Kelvin.label})

        if segundo == Temperatura.Celcius.value:
            if primeiro == Temperatura.Fahrenheit.value:
                valortemperatura = (valortemperatura * 9/5) + 32 +30
                self.validated_data.update({'resultado_conversao': valortemperatura})
                self._validated_data.update({'Temperatura': Temperatura.Fahrenheit.label})
            else:
                valortemperatura += 273.15
                self.validated_data.update({'resultado_conversao': valortemperatura})
                self._validated_data.update({'Temperatura': Temperatura.Kelvin.label})

        else:
            raise NotImplementedError('Operação Não Implementada')              
