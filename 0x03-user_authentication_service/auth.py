#!/usr/bin/env python3
"""
auth file
"""
from user import User
from db import DB
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    ''' Hash password '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    ''' Generate UUIDs '''
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' Register user '''
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            passwd = _hash_password(password)
            user = self._db.add_user(email, passwd)
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        ''' Credential validation '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), user.hashed_password)

    def create_session(self, email: str) -> str:
        '''  Get session ID '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id) -> User:
        ''' find user by session id '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id) -> None:
        ''' Destroy Session '''
        try:
            user = self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        ''' Generate reset password token '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        ''' Update password '''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hashed_password,
            reset_token=None)
