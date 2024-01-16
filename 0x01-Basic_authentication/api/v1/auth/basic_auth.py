#!/usr/bin/env python3
''' class BasicAuth that inherits from Auth '''
from .auth import Auth


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
