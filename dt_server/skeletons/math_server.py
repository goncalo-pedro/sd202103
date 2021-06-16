import game
import logging

import skeletons
import sockets


class MathServer:
    def __init__(self, port: int, jogo: game.Jogo) -> None:
        """
        Creates a client given the server server to use
        :param port: The math server port of the host the client will use
        """
        super().__init__()
        self._state = skeletons.SharedServerState(jogo, port)

    def run(self) -> None:
        """
        Runs the server server until the client sends a "terminate" action
        """
        skeletons.ServerControlSession(self._state).start()

        with sockets.Socket.create_server_socket(self._state.port, game.ACCEPT_TIMEOUT) as server_socket:
            logging.info("Waiting for clients to connect on port " + str(self._state.port))

            while self._state.keep_running:
                self._state.concurrent_clients.acquire()
                client_socket = server_socket.accept()
                if client_socket is not None:
                    self._state.add_client(client_socket)
                    skeletons.ClientSession(self._state, client_socket).start()
                else:
                    self._state.concurrent_clients.release()

            logging.info("Waiting for clients to terminate...")

        logging.info("Server stopped")
