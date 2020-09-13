from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import User


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserRegisterSerializer(ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(User.objects.all())])
    password = serializers.CharField()
    income = serializers.IntegerField()

    def validate(self, attrs):
        if attrs.get('password') != self.context['request'].data.pop('password2'):
            raise ValidationError({'password2': 'Passwords mismatch'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            income=validated_data['income']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'income')
