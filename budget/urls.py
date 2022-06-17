from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AccountViewSet, TransactionViewSet, StatsView

router = SimpleRouter()

router.register('accounts', AccountViewSet, basename="accounts")
router.register('transactions', TransactionViewSet, basename="transactions")

urlpatterns = router.urls
urlpatterns += [
    path('stats/', StatsView.as_view(), name="stats")
]
