from django_filters import rest_framework as filters
from core.models import Person

class PersonFilter(filters.FilterSet):
    
    class Meta:
        model = Person
        fields = ["nombre", "edad", "nacionalidad", "sexo"]

