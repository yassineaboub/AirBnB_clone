#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

time = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            if k == 'id':
                self.id = v
            elif k == 'created_at':
                    self.created_at = datetime.strptime(v, time)
            elif k == 'updated_at':
                    self.updated_at = datetime.strptime(v, time)
                    setattr(self, k, v)
        else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
    
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        the_dict = self.__dict__
        the_dict ['__class__'] = self.__class__.__name__
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        return the_dict
