from rest_framework import generics

from categories.models import Cat
from categories.serializers import CatSerializer

cats = Cat.objects.all()


class CatListCreateView(generics.ListCreateAPIView):
    queryset = cats
    serializer_class = CatSerializer


class CatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = cats
    serializer_class = CatSerializer

