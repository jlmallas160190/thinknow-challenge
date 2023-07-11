from django_filters import rest_framework as filters
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from .serializers import PersonResponseSerializer, PersonRequestSerializer
from .filter import PersonFilter
from core.models import Person

class PersonViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    serializer_class = PersonResponseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PersonFilter
    ordering_fields=["nombre","edad"]
    ordering=['nombre']

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
    
    def update(self, request, pk=None, *args, **kwargs):
        person = Person.objects.get(id=pk)
        serializer = PersonRequestSerializer(
            person, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)