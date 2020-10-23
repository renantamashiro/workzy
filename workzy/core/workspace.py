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

    @property
    def name(self) -> str:
        """Getter method that returns the name of the Workspace.

        :return: The name of the Workspace.
        :rtype: str.
        """
        return self._name

    @name.setter
    def name(self, name) -> None:
        """Setter method for name attribute.

        :param name: The name for this Workspace.
        """
        self._name = name

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
        self._jobs = jobs

    def append(self, command) -> None:
        """Add a new command for jobs attributes.

        :param command: new command to be added.
        :type command: str.
        """
        self._jobs.append(command)

    def remove(self, command: str) -> None:
        """Remove a workspace command.

        :param command: command to be removed.
        :type command: str.
        """
        self._jobs.remove(command)

    def initialize(self) -> None:
        """Calls the thread's start method
        and invokes the process's run method.
        """
        for command in self._jobs:
            process = Process(command)
            process.start()
