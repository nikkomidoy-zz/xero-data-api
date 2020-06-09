import json

from django.conf import settings
from django.core.cache import caches
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from xero.auth import OAuth2Credentials
from xero.constants import XeroScopes

from xero_auth.utils import get_oauth2_credentials_obj


class XeroUserLogin(APIView):
    def get(self, request, format=None):
        """
        Return a redirected login for Xero account Oauth
        """
        scopes = [
            XeroScopes.OFFLINE_ACCESS,
            XeroScopes.ACCOUNTING_CONTACTS,
            XeroScopes.ACCOUNTING_TRANSACTIONS,
            XeroScopes.OPENID,
            XeroScopes.PROFILE,
            XeroScopes.EMAIL,
        ]
        import pdb;pdb.set_trace()
        xero_client_id = request.GET.get('client_id', settings.XERO_CLIENT_ID)
        xero_client_secret = request.GET.get('client_secret', settings.XERO_CLIENT_SECRET)
        credentials = OAuth2Credentials(
            xero_client_id,
            xero_client_secret,
            callback_uri=settings.XERO_CALLBACK_URI,
            scope=scopes,
        )
        authorization_url = credentials.generate_url()
        request.user.xero_credentials = json.dumps(credentials.state)
        request.user.save()
        return HttpResponseRedirect(authorization_url)


class XeroProcessCallBack(APIView):
    def get(self, request, format=None):
        """
        Process callback URI after logging in
        """
        credentials = get_oauth2_credentials_obj(request.user, from_callback=True)
        auth_secret = request.get_raw_uri().replace("http", "https")
        credentials.verify(auth_secret)
        credentials.set_default_tenant()
        request.user.xero_credentials = json.dumps(credentials.state)
        request.user.save()
        success_message = "You have successfully connected your Xero account."
        return Response({"Success": success_message}, status=status.HTTP_200_OK)
