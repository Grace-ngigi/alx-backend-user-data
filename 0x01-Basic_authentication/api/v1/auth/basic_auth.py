#!/usr/bin/env python3
''' class BasicAuth that inherits from Auth '''
from .auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd:
                                     str) -> TypeVar('User'):
        ''' return user instance based on their email and password '''
        if not isinstance(user_email, str) or user_email is None:
            return None
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None
        
    def current_user(self, request=None) -> TypeVar('User'):
        ''' overloads user and retrieves User instance of a request '''
        auth_header = self.authorization_header(request)
        if  auth_header:
            token = self.extract_base64_authorization_header(auth_header)
            if token:
                decoded_str = self.decode_base64_authorization_header(token)
                if decoded_str:
                    email, passwd = self.extract_user_credentials(decoded_str)
                    if email:
                        return self.user_object_from_credentials(email, passwd)
        return            
