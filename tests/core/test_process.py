import unittest

from workzy.core import Process


class TestProcess(unittest.TestCase):
    """
    Test suite for process class
    """

    def setUp(self):
        self.process = Process("ls")

    def test_run_a_process(self):
        """Run a process that returns a string with the args"""
        self.assertEqual(self.process.run(), [self.process.command])
