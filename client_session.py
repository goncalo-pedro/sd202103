from threading import Thread
import logging

import game
import skeletons
import sockets


class ClientSession(Thread):
    """Maintains a session with the client"""

    def __init__(self, shared_state: skeletons.SharedServerState, client_socket: sockets.Socket):
        """
        Constructs a thread to hold a session with the client

        :param shared_state: The server's state shared by threads
        :param client_socket: The client's socket
        """
        Thread.__init__(self)
        self._shared_state = shared_state
        self._client_connection = client_socket

    def _add(self) -> None:
        a = self._client_connection.receive_int(game.INT_SIZE)
        b = self._client_connection.receive_int(game.INT_SIZE)
        result = self._shared_state.math_server.add(a, b)
        self._client_connection.send_int(result, game.INT_SIZE)

    def _sym(self) -> None:
        a = self._client_connection.receive_int(game.INT_SIZE)
        result = self._shared_state.math_server.sym(a)
        self._client_connection.send_int(result, game.INT_SIZE)

    def run(self):
        """Maintains a session with the client, following the established protocol"""
        with self._client_connection as client:
            logging.debug("Client " + str(client.peer_addr) + " just connected")
            last_request = False
            while not last_request:
                last_request = self.dispatch_request()
            logging.debug("Client " + str(client.peer_addr) + " disconnected")
            self._shared_state.remove_client(self._client_connection)
            self._shared_state.concurrent_clients.release()

    def dispatch_request(self) -> bool:
        request_type = self._client_connection.receive_str()
        last_request = False
        if request_type == game.ADD_OP:
            self._add()
        elif request_type == game.SYM_OP:
            self._sym()
        elif request_type == game.BYE_OP:
            last_request = True
        return last_request
