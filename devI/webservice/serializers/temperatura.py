from rest_framework import serializers 
from webservice.enumerations import Temperatura

class TemperaturaSerializer(serializers.Serializer):
    
    temperatura = serializers.FloatField(required=True)
    tipo = serializers.ChoiceField(required=True, choices=Temperatura)
    conversao = serializers.ChoiceField(required=True, choices=Temperatura)
    resultado = serializers.CharField(required=False)

    class Meta:
        fields = ['temperatura','tipo','conversao']

    def converter(self):

        temp_data = self.validated_data.get("temperatura")
        tipo_data = self.validated_data.get("tipo")
        conv_data = self.validated_data.get("conversao")

        match conv_data:
            
            # """Para converter para CELCIUS"""

            case Temperatura.CELCIUS:

                if tipo_data == Temperatura.CELCIUS:
                    self.validated_data.update({"resultado": temp_data})    

                elif tipo_data == Temperatura.FAHRENHEIT:
                    # multiplicar a temperatura em graus Celsius por 1,8 e somar 32
                    resultado = (temp_data * 1.8) + 32

                    self.validated_data.update({"resultado": str(resultado) + "°F"})    

                elif tipo_data == Temperatura.KELVIN:
                    # somar 273
                    resultado = temp_data + 273

                    self.validated_data.update({"resultado": str(resultado) + "°K"})

            case Temperatura.FAHRENHEIT:
                if tipo_data == Temperatura.CELCIUS:
                    # (Fahrenheit - 32) / 1.8
                    resultado = (temp_data - 32) / 1.8
                    self.validated_data.update({"resultado": str(resultado) + "°C"})

                elif tipo_data == Temperatura.FAHRENHEIT:
                    self.validated_data.update({"resultado": temp_data})

                elif tipo_data == Temperatura.KELVIN:
                    # (Fahrenheit - 32) * 5/9 + 273
                    resultado = ((temp_data - 32) / 1.8) + 273
                    self.validated_data.update({"resultado": str(resultado) + "K"})

            case Temperatura.KELVIN:
                if tipo_data == Temperatura.CELCIUS:
                    # Kelvin - 273
                    resultado = temp_data - 273
                    self.validated_data.update({"resultado": str(resultado) + "°C"})

                elif tipo_data == Temperatura.FAHRENHEIT:
                    # (Kelvin - 273) * 1.8 + 32
                    resultado = ((temp_data - 273) * 1.8) + 32
                    self.validated_data.update({"resultado": str(resultado) + "°F"})

                elif tipo_data == Temperatura.KELVIN:
                    self.validated_data.update({"resultado": temp_data})