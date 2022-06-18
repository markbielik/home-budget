from rest_framework import serializers

from .constants import TransactionTypeE
from .models import Accounts, Transactions


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = (
            'id',
            'user',
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
            'user',
            'amount',
            'description',
            'transaction_type',
            'transaction_type_display',
            'account',
            'created_data',
        )

    def get_transaction_type_display(self, obj):
        return TransactionTypeE(obj.transaction_type).name


class StatsFilterSerializer(serializers.Serializer):
    from_date = serializers.DateField(required=False)
    to_date = serializers.DateField(required=False)


class StatsResultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    amount_in = serializers.DecimalField(max_digits=15,
                                         decimal_places=2)
    amount_out = serializers.DecimalField(max_digits=15,
                                          decimal_places=2)
    balance = serializers.DecimalField(max_digits=15,
                                       decimal_places=2)


class StatsSerializer(serializers.Serializer):
    results = serializers.ListSerializer(child=StatsResultSerializer())
    date = StatsFilterSerializer()


