#!/usr/bin/env python3
"""
Test BaseModel class in base_model.py
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_type_basemodel(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_isstring(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_updated_isdatetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_unique_id(self):
        bmd1 = BaseModel().id
        bmd2 = BaseModel().id
        self.assertNotEqual(bmd1, bmd2)

    def test_created_and_updated_equal_when_not_change(self):
        bmd = BaseModel()
        self.assertEqual(bmd.created_at, bmd.updated_at)

    def test_updated_against_created_after_object_change(self):
        bmd = BaseModel()
        bmd.name = "FirstModel"
        bmd.number = 100
        bmd.save()
        self.assertLess(bmd.created_at, bmd.updated_at)
