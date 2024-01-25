#!/usr/bin/env python3
''' User DB Table '''

from sqlalchemy import Column, String, Boolean, Integer


class User():
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
