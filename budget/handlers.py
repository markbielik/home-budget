from budget.models import Transactions, Accounts


class AccountsAggregator:

    def __init__(self, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date
        filters = {}
        if self.from_date:
            filters["created_data__gte"] = self.from_date
        if self.to_date:
            filters["created_data__lte"] = self.to_date
        self.transactions_qs = Transactions.objects.filter(**filters)

    def aggregate(self):
        data = []
        for account in Accounts.objects.all():
            data.append(
                {
                    'id': account.id,
                    'name': account.name,
                    'amount_in': account.amount_in(transactions_qs=self.transactions_qs),
                    'amount_out': account.amount_out(transactions_qs=self.transactions_qs),
                    'balance': account.balance(transactions_qs=self.transactions_qs),
                }
            )
        return data
