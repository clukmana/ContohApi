import unittest
from django.test import TestCase
from .models import Transaction
from .serializers import TransactionSerializer
from .views import TransactionView
class TransactionModelTest(TestCase):
    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            customer_id=1,
            product_id=1,
            quantity=1,
            price=10.00,
            total_price=10.00,
        )
        self.assertEqual(transaction.customer_id, 1)
        self.assertEqual(transaction.product_id, 1)
        self.assertEqual(transaction.quantity, 1)
        self.assertEqual(transaction.price, 10.00)
        self.assertEqual(transaction.total_price, 10.00)
class TransactionSerializerTest(TestCase):
    def test_serialize_transaction(self):
        transaction = Transaction.objects.create(
            customer_id=1,
            product_id=1,
            quantity=1,
            price=10.00,
            total_price=10.00,
        )
        serializer = TransactionSerializer(transaction)
        self.assertEqual(serializer.data, {
            "id": 1,
            "customer_id": 1,
            "product_id": 1,
            "quantity": 1,
            "price": 10.00,
            "total_price": 10.00,
        })
class TransactionViewTest(TestCase):
    def test_list_transactions(self):
        transaction = Transaction.objects.create(
            customer_id=1,
            product_id=1,
            quantity=1,
            price=10.00,
            total_price=10.00,
        )
        response = self.client.get("/transactions/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "customer_id": 1,
                "product_id": 1,
                "quantity": 1,
                "price": 10. 0,
                "total_price": 10.00,
            }
        ])
    def test_create_transaction(self):
        data = {
            "customer_id": 1,
            "product_id": 1,
            "quantity": 1,
            "price": 10.00,
            "total_price": 10.00,
        }
        response = self.client.post("/transactions/", data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {
            "id": 1,
            "customer_id": 1,
            "product_id": 1,
            "quantity": 1,
            "price": 10.00,
            "total_price": 10.00,
        })
    def test_retrieve_transaction(self):
        transaction = Transaction.objects.create(
            customer_id=1,
            product_id=1,
            quantity=1,
            price=10.00,
            total_price=10.00,
        )
        response = self.client.get("/transactions/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            "id": 1,
            "customer_id": 1,
            "product_id": 1,
            "quantity": 1,
            "price": 10.00,
            "total_price": 10.00,
        })
    def test_update_transaction(self):
        transaction = Transaction.objects.create(
            customer_id=1,
            product_id=1,
            quantity=1,
            price=10.00,
            total_price=10.00,
        )
        data = {
            "customer_id": 2,
            "product_id": 2,
            "quantity": 2,
            "price": 20.00,
            "total_price": 20.00,
        }
         response = self.client.put("/transactions/1/", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            "id": 1,
            "customer_id": 2,
            "product_id": 2,
            "quantity": 2,
            "price": 20.00,
            "total_price": 20.00,
        })
    def test_delete_transaction(self):
        transaction = Transaction.objects.create(
            customer_id=1,
            product_id=1,
            quantity=1,
            price=10.00,
            total_price=10.00,
        )
        response = self.client.delete("/transactions/1/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
