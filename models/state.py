#!/usr/bin/python3
"""This is the state class"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import environ
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="states",
                          cascade="all, delete-orphan")

    if environ.get("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ getter attribute that connects relationship"""
            objects = models.storage.all()
            cities = []
            for k, v in objects.items():
                if "City" in k and v.state_id == self.id:
                    cities.append(v)
            return cities
