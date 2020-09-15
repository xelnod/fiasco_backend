from rest_framework import generics

from .models import Expense, OngoingExpense
from .serializers import ExpenseSerializer, OngoingExpenseSerializer

expenses = Expense.objects.all()
ongoing_expenses = OngoingExpense.objects.all()


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = expenses
    serializer_class = ExpenseSerializer


class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = expenses
    serializer_class = ExpenseSerializer


class OngoingExpenseListCreateView(generics.ListCreateAPIView):
    queryset = ongoing_expenses
    serializer_class = OngoingExpenseSerializer


class OngoingExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ongoing_expenses
    serializer_class = OngoingExpenseSerializer

