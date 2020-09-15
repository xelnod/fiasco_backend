from rest_framework import generics

from .models import Colour
from .serializers import ColourSerializer

colours = Colour.objects.all()


class ColourListCreateView(generics.ListCreateAPIView):
    queryset = colours
    serializer_class = ColourSerializer


class ColourRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = colours
    serializer_class = ColourSerializer

