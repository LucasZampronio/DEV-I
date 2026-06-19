from django.forms import ValidationError
from rest_framework import serializers


class MixinSerializerValidate:

    def validade(self, attrs):

        object = self.instance or self.Meta.model(**attrs)

        try:
            object.full_clean()

        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return attrs
