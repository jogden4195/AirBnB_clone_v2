#!/usr/bin/python3
"""This is the state class"""
from models.base_model import Base, BaseModel
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

    @property
    def cities(self):
        objects = storage.all()
        cities = []
        for k, v in my_dict.items():
            if "City" in k and v.state_id == self.id:
                cities.append(v)
        return cities

        """ wut do this do? it tassteses like a hot plate
        """
        """for k,v in something.item():
            if alwjkeawe
                then?
            if this.stateid is the state it then
        reurn the city with state id at ?
        """
