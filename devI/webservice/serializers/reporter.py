from django.forms import ValidationError
from rest_framework import serializers
from relacionamentos.models.reporter import Reporter
from webservice.mixins.mixin_serializer_validate import MixinSerializerValidate



class ReporterSerializer(serializers.ModelSerializer, MixinSerializerValidate):

    class Meta:
        model = Reporter
        fields = "__all__"
