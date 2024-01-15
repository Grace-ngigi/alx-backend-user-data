#!/usr/bin/env python3
''' class to manage the API authentication '''
from flask import request
from typing import List, TypeVar


class Auth:
    ''' class to manage the API authentication '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''  returns False - path and excluded_paths '''
        if path is None or excluded_paths is None or any(
            path.startswith(excluded) 
            or excluded.startswith(path) 
            or (excluded.endswith("*") 
                and path.startswith(excluded[:-1]))
        for excluded in excluded_paths
    ):
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        ''' returns None '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' returns None '''
        return None
