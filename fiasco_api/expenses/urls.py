from django.urls import path

from .views import ExpenseListCreateView, ExpenseRetrieveUpdateDestroyView, OngoingExpenseListCreateView, OngoingExpenseRetrieveUpdateDestroyView

urlpatterns = [
    path('', ExpenseListCreateView.as_view()),
    path('<int:pk>/', OngoingExpenseRetrieveUpdateDestroyView.as_view()),
    path('/o/', OngoingExpenseListCreateView.as_view()),
    path('/o/<int:pk>', OngoingExpenseRetrieveUpdateDestroyView)
]
