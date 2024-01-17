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
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for excluded_path in excluded_paths:
                if excluded_path.startswith(path):
                    return False
                if path.startswith(excluded_path):
                    return False
                if excluded_path[-1] == "*":
                    if path.startswith(excluded_path[:-1]):
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
