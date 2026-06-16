from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView, Response
from relacionamentos.models import Pessoa
from django.core.exceptions import ValidationError


class PersonMinimalSerializer(serializers.ModelSerializer):

    def validate(self, attrs):

        instancia = Pessoa(**attrs)
        
        try:
            instancia.full_clean()

        except ValidationError as errors:
            raise serializers.ValidationError(errors)

        return attrs
    
    class Meta:
        model = Pessoa
        fields = ["id", "nome"]


class PersonCompleteSerializer(serializers.ModelSerializer):

    def validate(self, attrs):

        instancia = Pessoa(**attrs)

        try:
            instancia.full_clean()

        except ValidationError as errors:
            raise serializers.ValidationError(errors)

        return attrs

    class Meta:
        model = Pessoa
        fields = "__all__"
