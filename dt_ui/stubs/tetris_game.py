import socket

from sockets.sockets_mod import Socket


class TetrisGame:
    """

    """

    def __init__(self, host: str, port: int):
        """

        :param host:
        :param port:
        """
        super().__init__()
        self._current_connection = Socket.create_client_socket(host, port)




# PYGAME STUFF:

    # K_LEFT:	1073741904
    # K_RIGHT:  1073741903
    # K_DOWN:	1073741905
    # K_UP:     1073741906

    def move_left(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741904, 10)
        return self._current_connection.receive_int(10)

    def move_right(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741903, 10)
        return self._current_connection.receive_int(10)

    def move_down(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741905, 10)
        return self._current_connection.receive_int(10)

    def move_up(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_int(1073741906, 10)
        return self._current_connection.receive_int(10)

    def get_shape(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("shape")
        return self._current_connection.receive_obj()

    def create_grid(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("grid")
        return self._current_connection.receive_obj()

    def get_locked_positions(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("getlocked")
        return self._current_connection.receive_obj()

    def set_locked_positions(self, locked_positions):
        """

        :param locked_positions:
        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("setlocked")
        self._current_connection.send_obj(locked_positions)

    def valid_space(self, piece):
        """

        :param piece:
        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("valid")
        self._current_connection.send_obj(piece)
        return self._current_connection.receive_obj()

    def clear_rows(self, grid):
        """

        :param grid:
        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("clear")
        self._current_connection.send_obj(grid)
        return self._current_connection.receive_int(10)

    def convert_shape_format(self, current_piece):
        """

        :param current_piece:
        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("convert")
        self._current_connection.send_obj(current_piece)
        return self._current_connection.receive_obj()

    def check_lost(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("lost")
        return self._current_connection.receive_int(10)

    def exit(self):
        """

        :return:
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("exit")

    def connect(self):
        """

        :return:
        """
        self._current_connection = socket.socket()



