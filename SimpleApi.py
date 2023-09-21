# Import the necessary modules.
from django.db import models
from django.urls import path, include
# Create the transaction model.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Transaction {self.id}"
# Create the transaction serializer.
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "customer_id", "product_id", "quantity", "price", "total_price")
# Create the transaction view.
class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
# Create the URL for transactions.
urlpatterns = [
    path("transactions/", TransactionView.as_view({"get": "list", "post": "create"})),
    path("transactions/<int:pk>/", TransactionView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]
