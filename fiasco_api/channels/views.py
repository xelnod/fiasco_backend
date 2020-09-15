from rest_framework import generics

from .models import Channel
from .serializers import ChannelSerializer

channels = Channel.objects.all()


class ChannelListCreateView(generics.ListCreateAPIView):
    queryset = channels
    serializer_class = ChannelSerializer


class ChannelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = channels
    serializer_class = ChannelSerializer

