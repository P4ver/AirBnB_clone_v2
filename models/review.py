#!/usr/bin/python3
"""This module defines the User class, a representation of a user in the AirBnB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class represents a user in the AirBnB project
    Attributes:
        email: The email address of the user
        password: The password for user login
        first_name: The first name of the user
        last_name: The last name of the user
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', backref='user',
                          cascade='all, delete-orphan')
    reviews = relationship('Review', backref='user',
                           cascade='all, delete-orphan')
