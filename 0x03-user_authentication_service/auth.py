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


def _generate_uuid():
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
