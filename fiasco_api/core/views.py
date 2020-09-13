from django.contrib.auth import login
from rest_framework import generics

from users.models import User
from users.serializers import UserRegisterSerializer

#
# class BuildViewSet(ModelViewSet):
#     serializer_class = BuildSerializer
#     queryset = Build.objects.all()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        new_user = User.objects.get(id=result.data['id'])
        new_user.populate_initial_models()
        login(self.request, new_user)
        return result
