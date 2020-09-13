from django.db import models
from django.conf import settings
from core.mixins import Trackable


class ExpenseProto(models.Model):
    tags = models.ManyToManyField('tags.Tag')
    kit = models.ForeignKey('categories.Kit', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255)
    channel = models.ForeignKey('channels.Channel', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    amount = models.IntegerField(default=0)

    @property
    def cat(self):
        return self.kit.cat


class Expense(Trackable, ExpenseProto):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_fulfilled = models.BooleanField(default=True)
    money_stored = models.BooleanField(default=False)
    ongoing_origin = models.ForeignKey('expenses.OngoingExpense', null=True, blank=True, default=None, on_delete=models.SET_NULL)


class OngoingExpenseScope(models.IntegerChoices):
    MONTH = 0, 'Month'
    YEAR = 1, 'Year'


class OngoingExpense(Trackable, ExpenseProto):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scope = models.IntegerField(
        choices=OngoingExpenseScope.choices,
        default=OngoingExpenseScope.MONTH,
    )
