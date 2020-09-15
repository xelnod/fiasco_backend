from rest_framework import generics

from .models import Tag
from .serializers import TagSerializer

tags = Tag.objects.all()


class TagListCreateView(generics.ListCreateAPIView):
    queryset = tags
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = tags
    serializer_class = TagSerializer

