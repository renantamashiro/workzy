from workzy.core.queue_process import QueueProcess


class Workspace:
    """Workspace organize different types of process (jobs) to run
    simultaneuosly. Each job it is a Thread that runs when
    the user call the workspace's name.

    :param name: A name for this workspace that will call
    by the user
    :type name: str
    """
    def __init__(self, name):
        self._name = name
        self._jobs = QueueProcess

    @property
    def name(self) -> str:
        """Getter method that returns the name of the Workspace.

        :return: The name of the Workspace
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name) -> None:
        """Setter method for name attribute

        :param name: The name for this Workspace
        """
        self._name = name

    @property
    def jobs(self) -> QueueProcess:
        """Getter method that returns all jobs associated with this Workspace.

        :return: A `QueueProcess` class that refers a process queue associated
        with this Workspace
        :rtype: class: `QueueProcess`
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: QueueProcess):
        """Setter method for jobs attribute

        :param jobs: A class:`QueueProcess` instance
        """
        self._jobs = jobs
