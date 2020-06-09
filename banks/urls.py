from django.urls import path

from banks.views import (BankTransactionsAPIView,
                         BankTransactionsInGoogleSheetAPIView)

urlpatterns = [
    path("transactions/", BankTransactionsAPIView.as_view(), name="transactions"),
    path(
        "transactions/spreadsheet/",
        BankTransactionsInGoogleSheetAPIView.as_view(),
        name="transactions_to_sheet",
    ),
]

app_name = "banks"
