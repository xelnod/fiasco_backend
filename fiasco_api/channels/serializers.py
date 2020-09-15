from rest_framework import serializers

from .models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Channel
        fields = '__all__'
