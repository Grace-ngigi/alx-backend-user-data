#!/usr/bin/env python3
"""
Session Auth class definition
"""
from .auth import Auth
from uuid import uuid4


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
