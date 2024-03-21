#!/usr/bin/env python3
import uuid
from datetime import datetime as dt


class BaseModel:
    """
    class: BaseModel
    attr:
        id: the id of each instance
        created_at: the time the instance is created
        updted_at: the time the instance is updated
    methods:
        save - updates the public instance attribute
        updated_at with the current datetime
        to_dict - returns a dictionary containing
        all keys/values of __dict__ of the instance
    """
    
    def __init__(self, *args, **kwargs):
        self.id = f"{uuid.uuid4()}"
        self.created_at = dt.now()
        self.updated_at = dt.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Return the class instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save - updates the public instance attribute updated_at
        with the current datetime
        Args:
            None
        Return:
            None
        """
        self.__dict__["updated_at"] = dt.now()

    def to_dict(self):
        """
        to_dict - returns a dictionary containing al
        keys/values of __dict__ of the instance
        Args:
            None
        Return:
            dict
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
