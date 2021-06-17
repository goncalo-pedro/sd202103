import sockets

import skeletons
from sockets.sockets_mod import Socket

import game


class TetrisServer(Socket):
    """
        TetrisServer é a classe responsável pela função de stub,
        recebe e responde a pedidos feito pelo cliente
    """
    def __init__(self, port: int, jogo: game.Jogo):
        """
            Constrói um objeto "TetrisServer"

        :param port: int
        :param jogo: Jogo
        """
        super().__init__()
        self._state = skeletons.SharedServerState(jogo, port)

    def run(self) -> None:
        """
        Abre o socket para que o cliente comece a sua comunicação,
        fazendo pedidos para as devidas respostas.

        :return: returns nothing
        :rtype: None
        """

        """
                Runs the server server until the client sends a "terminate" action
                """
        with sockets.Socket.create_server_socket(self._state.port, game.ACCEPT_TIMEOUT) as server_socket:
            print("Waiting for clients to connect on port " + str(self._state.port))

            while self._state.keep_running:
                self._state.concurrent_clients.acquire()
                client_socket = server_socket.accept()
                if client_socket is not None:
                    self._state.add_client(client_socket)
                    skeletons.ClientSession(self._state, client_socket).start()
                else:
                    self._state.concurrent_clients.release()

            print("Waiting for clients to terminate...")

        print("Server stopped")
