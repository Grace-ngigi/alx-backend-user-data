#!/usr/bin/env python3
"""
Session Auth class definition
"""
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    ''' Session Auth class definition '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' create session id '''
        if user_id is None or not isinstance(user_id, str):
            return None
        rand_id = uuid4()
        self.user_id_by_session_id[str(rand_id)] = user_id
        return str(rand_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' returns a User ID based on a Session ID '''
        if not isinstance(session_id, str) or session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)
    