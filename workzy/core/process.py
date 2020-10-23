import subprocess
from threading import Thread


class Process(Thread):
    """A simple thread that runs each command
    associated with a specific workspace.

    :param command: command to call a program.
    """
    def __init__(self, command):
        Thread.__init__(self)
        self._command = command

    def run(self) -> None:
        """Calls a subprocess module that run a command."""
        subprocess.run(self.command)

    @property
    def command(self) -> str:
        """Getter method that returns the command associated
        with this thread."""
        return self._command
