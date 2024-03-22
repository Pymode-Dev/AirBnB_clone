#!/usr/bin/env python3
"""
A class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances.
"""

import json

class FileStorage:
    """
    class:
        FileStorage - it serializes class instances into JSON
        format and file, then back to class instance from JSON format.
    Attrs:
        __file_path: the json filepath
        __objects: the class dict objects to transform to JSON format
    Methods:
        all: returns the __objects
        new: sets in __objects the obj with key <obj class name>.id
        save: serializes __objects to the JSON file (path: __file_path)
        reload:  deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist
        no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"
        returns the _objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]

    def sav(self):
        """
        save __objects in JSON format into file.
        """
        fpath = FileStorage.__objects
        ndict = {obj: fpath[obj].to_dict() for obj in fpath}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(ndict, f)
