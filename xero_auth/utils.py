import json

from xero.auth import OAuth2Credentials


def get_oauth2_credentials_obj(user_obj, from_callback=False):
    """
    Get credential object from OAuth2 in Pyxero
    """
    cred_state = json.loads(user_obj.xero_credentials)
    credentials = OAuth2Credentials(**cred_state)
    if not from_callback and credentials.expired():
        credentials.refresh()
        user_obj.xero_credentials = json.dumps(credentials.state)
        user_obj.save()

    return credentials
