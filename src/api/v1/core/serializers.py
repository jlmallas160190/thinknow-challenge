from rest_framework import serializers
from core.models import Person
class PersonResponseSerializer(serializers.ModelSerializer):
    """Person response serializer."""

    class Meta:
        model = Person
        read_only_fields = [
            "id",
            "nombre",
            "nacionalidad",
            "sexo",
            "edad",
        ]
        fields = read_only_fields

class PersonRequestSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Person
        fields = (
            "nombre",
            "nacionalidad",
            "sexo",
            "edad",
        )