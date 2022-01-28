from abc import ABC, abstractmethod


class AbstractCloudManager(ABC):
    __slots__ = ('_handler',)

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """
        Tha basic constructor. Creates a new instance using the specified credentials
        """

        pass

    @staticmethod
    @abstractmethod
    def get_handler(*args, **kwargs):
        """
        Returns a CloudManager handler.

        :param args:
        :param kwargs:
        :return:
        """

        pass

    @abstractmethod
    def upload_file(self, *args, **kwargs):
        """
        Uploads a file to the CloudManager

        :param args:
        :param kwargs:
        :return:
        """

        pass

    @abstractmethod
    def download_file(self, *args, **kwargs):
        """
        Downloads a file from the CloudManager

        :param args:
        :param kwargs:
        :return:
        """

        pass

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        """
        Deletes a file from the CloudManager

        :param args:
        :param kwargs:
        :return:
        """

        pass

    @abstractmethod
    def ls(self, *args, **kwargs):
        """
        List the files and folders in the CloudManager
        :param args:
        :param kwargs:
        :return:
        """
        pass
