#!/usr/bin/python3
""" added comment """
import json
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ SQL database class
    """
    __engine = None
    __Session = None

    def __init__(self):
        """ the initializersz
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            environ['HBNB_MYSQL_USER'],
            environ['HBNB_MYSQL_PWD'],
            environ['HBNB_MYSQL_HOST'],
            environ['HBNB_MYSQL_DB']),
                               pool_pre_ping=True)
        if 'HBNB_ENV' in environ.keys():
            if environ['HBNB_ENV'] == 'test':
                # This might not be correct tbh
                drop_all(self.__engine)
        # Does session go here?
        # self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None):
        """ returns a dictionary of all objects """
        # Or here???
        # self.__session = sessionmaker(bind=self.__engine)
        my_dict = {}
        if cls is None:
            for c in [State, City]:
                for obj in self.__session.query(c).all():
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    my_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = cls + '.' + str(obj.id)
                my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """ adds object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(obj).delete(synchronize_session=False)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False))
