from abc import ABCMeta, abstractmethod
from typing import Any
from XSocket.core.net import AddressInfo

__all__ = [
    "ISocket"
]


class ISocket(metaclass=ABCMeta):
    """
    Implements sockets interface.
    """

    @property
    @abstractmethod
    def get_raw_socket(self) -> Any:
        """
        Get a low-level socket.

        :return: Low-level socket
        """

    @property
    @abstractmethod
    def local_address(self) -> AddressInfo:
        """
        Gets the local address info.

        :return: AddressInfo
        """

    @property
    @abstractmethod
    def remote_address(self) -> AddressInfo:
        """
        Gets the remote address info.

        :return: AddressInfo
        """

    @abstractmethod
    def close(self):
        """
        Close the socket.
        """

    @abstractmethod
    async def send(self, data: bytearray):
        """
        Sends data to a connected Socket.

        :param data: Data to send
        """

    @abstractmethod
    async def receive(self, length: int, exactly: bool = False) -> bytearray:
        """
        Receives data from a bound Socket.

        :param length: The number of bytes to receive
        :param exactly: Weather to read exactly
        :return: Received data
        """
