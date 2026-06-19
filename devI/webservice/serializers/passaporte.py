from rest_framework import serializers  
from relacionamentos.models.passaporte import Passaporte

class PassaporteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passaporte
        fields = "__all__"