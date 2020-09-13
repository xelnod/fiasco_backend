from rest_framework import serializers

from categories.models import Cat


class CatSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cat
        fields = '__all__'
