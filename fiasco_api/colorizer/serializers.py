from rest_framework import serializers

from .models import Colour


class ColourSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Colour
        fields = '__all__'
