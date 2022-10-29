#!/usr/bin/python3

import uuid
import models
from datetime import datetime

class BaseModel:
    """BaseModel Class Details"""
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%F")
                    if key == "__class__":
                        continue
                    setattr(self, key, value)

                else:
                     self.id = uuid4()
                     self.created_at = datetime.now()
                     self.updated_at = datetime.now()

    def __str__(self):
        tmp = '[{}] ({}) {}'
        return tmp.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
        return

    def to_dict(self):
        new_dictionary = self.__dict__.copy()
        new_dictionary.update({'__class__':str(self.__class__.name__)})
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()
        return new_dictionary
