from django.urls import path

from .views import TagListCreateView, TagRetrieveUpdateDestroyView

urlpatterns = [
    path('', TagListCreateView.as_view()),
    path('<int:pk>/', TagRetrieveUpdateDestroyView.as_view()),
]
