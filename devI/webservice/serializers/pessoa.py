from rest_framework import serializers
from relacionamentos.models import Pessoa


class PersonMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id','nome']