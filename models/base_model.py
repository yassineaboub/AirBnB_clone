#!/usr/bin/python3
import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        the_dict = self.__dict__
        the_dict ['__class__'] = self.__class__.__name__
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        return the_dict
