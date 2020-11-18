import unittest

from workzy.core import Workspace


class TestWorkspace(unittest.TestCase):
    """
    Workspace's test suite
    """

    def setUp(self):
        self.workspace = Workspace("Dummy")

    def test_correct_type_name(self):
        """
        Set a valid name for an workspace and test it
        """
        self.assertEqual(self.workspace.name, "Dummy")
        name = "Great Dummy"
        self.workspace.name = name
        self.assertEqual(self.workspace.name, name)

    def test_invalid_name(self):
        """
        Set a invalid name for an workspace and test it
        """
        name = 123

        with self.assertRaises(TypeError):
            self.workspace.name = name

    def test_valid_jobs_list(self):
        """
        Set a list of jobs (commands)
        """
        jobs = ["command1", "command2", "command3"]

        self.workspace.jobs = jobs
        self.assertIsInstance(self.workspace.jobs, list)
        self.assertEqual(self.workspace[1], jobs[1])

    def test_invalid_jobs_list(self):
        """
        Set a invalid type of list for an workspace
        """
        jobs = ("command1", "command2", "command3")

        with self.assertRaises(TypeError):
            self.workspace.jobs = jobs

    def test_append_jobs_method(self):
        """
        Append a valid command for jobs
        """
        command = "command4"
        self.workspace.append(command)
        self.assertEqual(self.workspace[0], command)

    def test_append_invalid_command(self):
        """
        Append a invalid command for jobs
        """
        command = 123
        with self.assertRaises(TypeError):
            self.workspace.append(command)

    def test_remove_command(self):
        """
        Remove a command in workspace's jobs
        """
        commands = ["command1", "command2", "command3"]
        self.workspace.jobs = commands
        self.workspace.remove("command1")
        self.assertEqual(len(self.workspace), 2)
        self.assertEqual(self.workspace[0], "command2")
