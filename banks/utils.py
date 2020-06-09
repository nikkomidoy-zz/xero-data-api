import gspread
from django.conf import settings
from gspread.utils import absolute_range_name
from xero import Xero


def get_all_bank_transactions(credentials):
    """
    Fetch all bank transactions
    """
    xero = Xero(credentials)
    return xero.banktransactions.all()


def post_transactions_to_google_sheets(transactions):
    """
    Record transactions in google sheets
    """
    google_creds = gspread.service_account(filename="google-api-creds.json")
    google_sheet = google_creds.open(settings.GOOGLE_SHEET_NAME)
    worksheet = google_sheet.get_worksheet(0)
    headers = worksheet.row_values(1)
    put_values = []
    for v in transactions:
        temp = []
        for h in headers:
            temp.append(v[settings.GOOGLE_SHEET_HEADERS_TO_KEY[h]])
        put_values.append(temp)

    worksheet.append_rows(put_values)
