from rest_framework import serializers

from .models import Expense, OngoingExpense


class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Expense
        fields = '__all__'


class OngoingExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = OngoingExpense
        fields = '__all__'
