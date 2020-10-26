import unittest

from workzy.core import Process


class TestProcess(unittest.TestCase):
    """
    Test suite for process class
    """
    def setUp(self):
        self.process = Process("")