#!/usr/bin/env python3
''' class BasicAuth that inherits from Auth '''
from .auth import Auth
import base64


class BasicAuth(Auth):
    '''BasicAuth inerits from Auth'''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        ''' Extracts the Base64 part of the Authorization header '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        value = authorization_header.split(" ")[-1]
        return value

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        ''' returns te decoded value of  Base64 Strin '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_str = base64_authorization_header.encode('utf-8')
            decoded_str = base64.b64decode(decoded_str)
            return decoded_str.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        ''' returns user email and password from Base64 decoded value '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email = decoded_base64_authorization_header.split(":")[0]
        passwd = decoded_base64_authorization_header.split(":")[1]
        return (email, passwd)
