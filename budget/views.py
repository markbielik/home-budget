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
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Accounts.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
