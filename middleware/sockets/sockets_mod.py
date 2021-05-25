import pickle
from socket import socket, timeout
from typing import Union

import sockets


class Socket:
    """

    """
    def __init__(self):
        """
        Construtor
        """
        self._current_connection = None

    @property
    def current_connection(self):
        """

        :return: retorna conexão atual
        """
        return self._current_connection

    @current_connection.setter
    def current_connection(self, value):
        """
        altera o valor de value para conectar
        :param value: int
        :return: None
        """
        self._current_connection = value

    def accept(self) -> Union['Socket', None]:
        try:
            client_connection, _ = self._current_connection.accept()
            new_socket = Socket()
            new_socket.current_connection = client_connection
            return new_socket
        except timeout:
            return None

    @property
    def peer_add(self):
        return self._current_connection.getpeername()

    def receive_int(self, n_bytes: int) -> int:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next integer read from the current connection
        """
        data = self._current_connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, value: int, n_bytes: int) -> None:
        """
        :param value: The integer value to be sent to the current connection
        :param n_bytes: The number of bytes to send
        """
        self._current_connection.send(value.to_bytes(n_bytes, byteorder='big', signed=True))

    def receive_str(self) -> str:
        """
        :return: The next string read from the current connection
        """
        n_bytes: int = self.receive_int(sockets.INT_SIZE)
        received: bytes = self._current_connection.recv(n_bytes)
        return received.decode()

    def send_str(self, value: str) -> None:
        """
        :param value: The string value to send to the current connection
        """
        to_send: bytes = value.encode()
        self.send_int(len(to_send), sockets.INT_SIZE)
        self._current_connection.send(to_send)

    def send_obj(self, obj):
        """

        :param obj: the object value to send to the current connection
        :return:
        """
        data: bytes = pickle.dumps(obj)
        self.send_int(len(data), sockets.INT_SIZE)
        self._current_connection.send(data)

    def receive_obj(self):
        """
        :return: The object to read from the current connection
        """
        n_bytes: int = self.receive_int(sockets.INT_SIZE)
        received: bytes = self._current_connection.recv(n_bytes)
        return pickle.loads(received)

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def close(self):
        if self._current_connection is not None:
            self._current_connection.close()

    @staticmethod
    def create_server_socket(port: int, timeout: int = None) -> 'Socket':
        new_socket: socket = socket()
        new_socket.bind(('', port))
        new_socket.listen(1)
        new_socket.settimeout(timeout)

        socket_middleware = Socket()
        socket_middleware.current_connection = new_socket
        return socket_middleware

    @staticmethod
    def create_client_socket(host: str, port: int) -> 'Socket':
        new_socket: socket = socket()
        new_socket.connect((host, port))

        socket_middleware = Socket()
        socket_middleware.current_connection = new_socket
        return socket_middleware
