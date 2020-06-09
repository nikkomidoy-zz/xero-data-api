from django.urls import path

from xero_auth.views import XeroProcessCallBack, XeroUserLogin

urlpatterns = [
    path("login/", XeroUserLogin.as_view(), name="xero_login"),
    path("process/callback/", XeroProcessCallBack.as_view(), name="xero_callback"),
]

app_name = "xero_auth"
