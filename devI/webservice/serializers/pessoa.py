from rest_framework import serializers
from relacionamentos.models.pessoa import Pessoa
from django.core.exceptions import ValidationError


class PessoaMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id','nome']


    def validate(self, attrs):
        pessoa = Pessoa(attrs)
        try:
            pessoa.full_clean()
        except ValidationError as erros:
            raise serializers.ValidationError(erros.message_dict)
        

class PessoaCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def validate(self, attrs):
        pessoa = self.instance
        try:
            pessoa.full_clean()
        except ValidationError as erros:
            raise serializers.ValidationError(erros.message_dict)
        