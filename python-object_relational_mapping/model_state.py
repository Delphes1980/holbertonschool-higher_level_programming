#!/usr/bin/python3
"""
This module defines the State model for a database, using SQLAlchemy's
declarative base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a base class for declarative models.
# This Base class will be inherited by all SQLAlchemy models to map Python
# classes to database tables.
Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in the database.

    This class defines the structure of the 'states' table, including its
    column names, data types, and constraints, using SQLAlchemy's declarative
    style. It maps Python class attributes to database columns
    """
    # Define the name of the table in the database
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
