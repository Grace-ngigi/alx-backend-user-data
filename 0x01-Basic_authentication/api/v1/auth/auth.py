#!/usr/bin/env python3
''' class to manage the API authentication '''
from flask import request
from typing import List, TypeVar


class Auth:
    ''' class to manage the API authentication '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''  returns False - path and excluded_paths '''
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/') + '/'
        if excluded_paths.endswith('*') and path.startswith(excluded_paths[:-1]):
            return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' returns None '''
        if request is None:
            return None
        eader = request.headers.get('Authorization')
        if eader is None:
            return None
        return eader

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns None '''
        return None
