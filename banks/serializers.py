from rest_framework import serializers


class BankTransactionsSerializers(serializers.Serializer):
    id = serializers.CharField(max_length=40)
    type = serializers.CharField()
    reference = serializers.CharField()
    is_reconciled = serializers.BooleanField()
    has_attachments = serializers.BooleanField()
    status = serializers.CharField()
    line_amount_types = serializers.CharField()
    subtotal = serializers.DecimalField(max_digits=4, decimal_places=2)
    total_tax = serializers.DecimalField(max_digits=4, decimal_places=2)
    total = serializers.DecimalField(max_digits=4, decimal_places=2)
    updated_date = serializers.DateTimeField()
    currency_code = serializers.CharField()
