from django.db.models import Sum
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .constants import TransactionTypeE
from .handlers import AccountsAggregator
from .models import Accounts, Transactions
from .serializers import AccountSerializer, TransactionSerializer, StatsSerializer, StatsFilterSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class StatsView(APIView):

    def get(self, request, *args, **kwargs):
        filter_account_stats = StatsFilterSerializer(data=request.query_params)
        filter_account_stats.is_valid(raise_exception=True)

        aggregator = AccountsAggregator(from_date=filter_account_stats.validated_data.get("from_date"),
                                        to_date=filter_account_stats.validated_data.get("to_date"))

        return Response(data=StatsSerializer(
            {'results': aggregator.aggregate(),
             'date': {
                 'from_date': aggregator.from_date,
                 'to_date': aggregator.to_date,
             }}).data)
