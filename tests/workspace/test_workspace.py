import unittest

from workzy.core.workspace import Workspace


class WorkspaceTestCase(unittest.TestCase):
    def setUp(self):
        self.workspace = Workspace("Dummy")

    def test_workspace_instance(self):
        self.assertIsInstance(self.workspace, Workspace)
