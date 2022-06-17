from rest_framework import serializers

from .constants import TransactionTypeE
from .models import Accounts, Transactions


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = (
            'id',
            'name',
            'description',
            'initial_balance'
        )


class TransactionSerializer(serializers.ModelSerializer):
    transaction_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Transactions
        fields = (
            'id',
            'amount',
            'description',
            'transaction_type',
            'transaction_type_display',
            'account'
        )

    def get_transaction_type_display(self, obj):
        return TransactionTypeE(obj.transaction_type).name

