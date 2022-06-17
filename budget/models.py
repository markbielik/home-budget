from django.db import models

from budget.constants import TransactionTypeE


class Accounts(models.Model):
    name = models.CharField(verbose_name="Account name",
                            max_length=256)
    description = models.CharField(max_length=2048,
                                   null=True,
                                   blank=True)
    initial_balance = models.DecimalField(verbose_name="Initial balance",
                                          max_digits=15,
                                          decimal_places=2)


class Transactions(models.Model):
    amount = models.DecimalField(verbose_name="Amount",
                                 max_digits=15,
                                 decimal_places=2)
    description = models.CharField(max_length=2048,
                                   null=True,
                                   blank=True)
    transaction_type = models.SmallIntegerField(verbose_name="Transaction type",
                                                choices=[
                                                    (transaction_type.value,
                                                     transaction_type.name) for transaction_type in TransactionTypeE])
    account = models.ForeignKey(Accounts,
                                on_delete=models.CASCADE)
