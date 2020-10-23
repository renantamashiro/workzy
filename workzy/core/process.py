import subprocess
from threading import Thread


class Process(Thread):
    def __init__(self, command):
        Thread.__init__(self)
        self._command = command

    def run(self):
        subprocess.run(self.command)

    @property
    def command(self):
        return self._command


def get_os():
    pass


def filter_commands_by_os(pid):
    pass
