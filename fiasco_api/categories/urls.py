from django.urls import path

from categories.views import CatListCreateView, CatRetrieveUpdateDestroyView

urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>/', CatRetrieveUpdateDestroyView.as_view()),
]
