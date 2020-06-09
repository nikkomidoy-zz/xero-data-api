from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from banks.utils import (get_all_bank_transactions,
                         post_transactions_to_google_sheets)
from xero_auth.utils import get_oauth2_credentials_obj


class BankTransactionsAPIView(APIView):
    def get(self, request, **kwargs):
        credentials = get_oauth2_credentials_obj(request.user)
        bank_transactions = get_all_bank_transactions(credentials)
        return Response(bank_transactions, status=status.HTTP_200_OK)


class BankTransactionsInGoogleSheetAPIView(APIView):
    def get(self, request, **kwargs):
        credentials = get_oauth2_credentials_obj(request.user)
        bank_transactions = get_all_bank_transactions(credentials)
        post_transactions_to_google_sheets(bank_transactions)

        success_message = f"You have successfully posted bank transactions to {settings.GOOGLE_SHEET_NAME} spreadsheet"
        return Response({"Success": success_message}, status=status.HTTP_200_OK)
