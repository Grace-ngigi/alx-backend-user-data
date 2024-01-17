#!/usr/bin/env python3
''' class to manage the API authentication '''
from flask import request
from typing import List, TypeVar


class Auth:
    ''' class to manage the API authentication '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''  returns False - path and excluded_paths '''
        if path is not None and excluded_paths is not None:
            for excluded_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if excluded_path[-1] == '*':
                    pattern = '{}.*'.format(excluded_path[0:-1])
                elif excluded_path[-1] == '/':
                    pattern = '{}/*'.format(excluded_path[0:-1])
                else:
                    pattern = '{}/*'.format(excluded_path)
                if re.match(pattern, path):
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
