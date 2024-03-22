#!/usr/bin/env python3
"""
test  file_storage.py
"""


import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_all_type(self):
        bmd = FileStorage()
        self.assertEqual(type(bmd), FileStorage)
