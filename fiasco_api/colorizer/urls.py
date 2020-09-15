from django.urls import path

from .views import ColourListCreateView, ColourRetrieveUpdateDestroyView

urlpatterns = [
    path('', ColourListCreateView.as_view()),
    path('<int:pk>/', ColourRetrieveUpdateDestroyView.as_view()),
]
