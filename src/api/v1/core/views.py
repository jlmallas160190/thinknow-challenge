from django_filters import rest_framework as filters
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from .serializers import PersonResponseSerializer, PersonRequestSerializer
from core.models import Person

class PersonViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = PersonResponseSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        return Person.objects.all()

    def create(self, request):
        serializer = PersonRequestSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
