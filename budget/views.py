from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Accounts, Transactions
from .serializers import AccountSerializer, TransactionSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer


class StatsView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(data={'info': 'stats view'})
