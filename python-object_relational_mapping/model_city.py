#!/usr/bin/python3
"""
This module defines the City model for a database, using SQLAlchemy's
declarative base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents the 'cities' table in the database.

    This class defines the structure of the 'cities' table, including its
    column names, data types, and constraints, using SQLAlchemy's declarative
    style. It maps Python class attributes to database columns
    """
    # Define the name of the table in the database
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
