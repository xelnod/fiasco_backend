from django.urls import path

from .views import ChannelListCreateView, ChannelRetrieveUpdateDestroyView

urlpatterns = [
    path('', ChannelListCreateView.as_view()),
    path('<int:pk>/', ChannelRetrieveUpdateDestroyView.as_view()),
]
