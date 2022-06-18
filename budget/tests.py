from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from budget.models import Accounts


class AccountTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.account = Accounts.objects.create(
            name="test account",
            initial_balance=0,
        )
        self.urls = {
            'list': reverse("accounts-list"),
            'detail': reverse("accounts-detail", args=(self.account.id,))
        }

    def test_list(self):
        response = self.client.get(self.urls['list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        self.assertEqual(response.data[0]['id'], self.account.id)

    def test_detail(self):
        response = self.client.get(self.urls['detail'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.account.id)

    def test_create(self):
        response = self.client.post(self.urls['list'], data={
            "name": "test account",
            "initial_balance":  100,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['initial_balance'], '100.00')

    def test_update(self):
        response = self.client.put(self.urls['detail'], data={
            "name": "new account",
            "initial_balance": 535,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new account')

    def test_partial_update(self):
        response = self.client.patch(self.urls['detail'], data={
            "name": "special account",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'special account')
