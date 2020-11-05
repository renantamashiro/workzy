import unittest

from workzy.core import db
from workzy.core.workspace import Workspace


class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.create_table()
        self.workspace = Workspace("Dummy")
        self.workspace.minutes = 50

    def test_db_insert_method(self):
        self.db.insert(self.workspace)

    def test_db_select_method(self):
        self.db.select(self.workspace)
