#!/usr/bin/env python3
''' class to manage the API authentication '''
from flask import request
from typing import List, TypeVar
import re
import os


class Auth:
    ''' class to manage the API authentication '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''  returns False - path and excluded_paths '''
        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/') + '/'
        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' returns None '''
        if request is None:
            return None
        eader = request.headers.get('Authorization')
        if eader is None:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns None '''
        return None

    def session_cookie(self, request=None):
        ''' returns a cookie value from a request '''
        if request is None:
            return None
        _my_session_id = os.getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
