#!/usr/bin/env python3
''' class to manage the API authentication '''
from flask import request
from typing import List, TypeVar

class Auth:
    ''' class to manage the API authentication '''
    pass

def require_auth(self, path: str, excluded_paths: List[str]):
    '''  returns False - path and excluded_paths '''
    return False

def authorization_header(self, request=None) -> str:
    ''' returns None '''
    return None

def current_user(self, request=None) -> TypeVar('User'):
    ''' returns None '''
    return None