from datetime import date

from workzy.core.process import Process


class Workspace:
    """Workspace organize different types of process (jobs) to run
    simultaneuosly. Each job it is a Thread that runs when
    the user call the workspace's name.

    :param name: A name for this workspace that will call by the user.
    :type name: str.
    """

    def __init__(self, name):
        self._name = name
        self._jobs = list()
        self._minutes = 0
        self._date = str(date.today().isoformat())

    def __len__(self):
        """Returns workspace's size"""
        return len(self._jobs)

    def __getitem__(self, index: int) -> str:
        """Returns a command listed by jobs attribute.

        :param index: command's position.
        :rtype: int.
        :return: Command
        """
        return self._jobs[index]

    @property
    def name(self) -> str:
        """Getter method that returns the name of the Workspace.

        :return: The name of the Workspace.
        :rtype: str.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Setter method for name attribute.

        :param name: The name for this Workspace.
        """
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Only `str` type for workspace's name")

    @property
    def jobs(self) -> list:
        """Getter method that returns all jobs associated with this Workspace.

        :return: A `list` that refers a process associated with this Workspace.
        :rtype: class: `list`.
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: list) -> None:
        """Setter method for jobs attribute.

        :param jobs: `list` instance.
        """
        if isinstance(jobs, list):
            self._jobs = jobs
        else:
            raise TypeError("Only `list` type for workspace's jobs")

    def append(self, command: str) -> None:
        """Add a new command for jobs attributes.

        :param command: new command to be added.
        :type command: str.
        """
        if isinstance(command, str):
            self._jobs.append(command)
        else:
            raise TypeError("Only `str` type for workspace's jobs")

    def remove(self, command: str) -> None:
        """Remove a workspace command.

        :param command: command to be removed.
        :type command: str.
        """
        self._jobs.remove(command)

    @property
    def minutes(self):
        """Getter method that minutes worked.
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Setter method for minutes worked.
        """
        self._minutes = minutes

    def date(self):
        """Getter method that returns a date.
        """
        return self._date

    def initialize(self) -> None:
        """Calls the thread's start method
        and invokes the process's run method.

        -Needs a counter
        """
        for command in self._jobs:
            process = Process(command)
            process.run()
