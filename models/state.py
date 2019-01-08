#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column("name",
                  String(128),
                  nullable=False)
    cities = relationship("City", backref=backref(
                          "state", cascade="all, delete"))

    def cities(self):
        """ wut do this do? it tassteses like a hot plate
        """
        for k,v in something.item():
            if alwjkeawe
                then?
            if this.stateid is the state it then
        reurn the city with state id at ?
 
