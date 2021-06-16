from threading import Thread
import logging

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

    def get_shape(self) -> None:
        """
        Comunica ao jogo que pretende obter o formato da peça
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :return: returns nothing
        :rtype: None
        """
        shape = self._shared_state.jogo.get_shape()
        self._client_connection.send_obj(shape)

    def create_grid(self) -> None:
        """
        Comunica ao jogo que pretende obter o formato da grelha do jogo
        com as devidas posições ocupadas.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :return: returns nothing
        :rtype: None
        """
        grid = self._shared_state.jogo.create_grid()
        self._client_connection.send_obj(grid)

    def get_locked_positions(self) -> None:
        """
        Comunica ao jogo que pretende obter o map de posições ocupadas.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :return: returns nothing
        :rtype: None
        """
        locked_positions = self._shared_state.jogo.get_locked_positions()
        self._client_connection.send_obj(locked_positions)

    def set_locked_positions(self, locked_positions: {}) -> None:
        """
        Comunica ao jogo que pretende alterar as posições ocupadas pelas peças.

        :param locked_positions: Map com as posições preenchidas pelas peças
        :type locked_positions: {}

        :return: returns nothings
        :rtype: None
        """
        self._shared_state.jogo.set_locked_positions(locked_positions)

    def valid_space(self, piece: [[]]) -> None:
        """
        Comunica ao jogo que pretende verificar se existe espaço disponível para a movimentação da peça.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :param piece: Matriz que representa o formato da peça
        :type piece: [[]]

        :return: returns nothing
        :rtype: None
        """
        valid_space = self._shared_state.jogo.valid_space(piece)
        self._client_connection.send_int(valid_space, 2)

    def clear_rows(self, grid: [[]]) -> None:
        """
        Comunica ao jogo que pretende verificar se existe espaço disponível para a movimentação da peça.
        Envia a resposta do jogo para o stub via middleware, em formato de inteiro.

        :param grid: Matriz que representa a grelha do tabuleiro, onde as pessoas se encontram
        :type grid: [[]]

        :return: returns nothing
        :rtype None
        """
        rows_cleared = self._shared_state.jogo.clear_rows(grid)
        self._client_connection.send_int(rows_cleared, 2)

    def convert_shape_format(self, current_piece: object) -> None:
        """
        Comunica ao jogo que pretende converter o formato da forma da peça escolhida
        para o desenho da mesma em posições na grelha do tabuleiro.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :param current_piece: Matriz que representa o formato da peça
        :type current_piece: object

        :return: returns nothing
        :rtype: None
        """
        shape = self._shared_state.jogo.convert_shape_format(current_piece)
        self._client_connection.send_obj(shape)

    def check_lost(self):
        """
        Comunica ao jogo que pretende verificar se o jogar já perdeu ou ainda continua a jogar.
        Envia a resposta do jogo para o stub via middleware, em formato de inteiro.

        :return: returns nothing
        :rtype: None
        """
        lost = self._shared_state.jogo.check_lost()
        self._client_connection.send_int(lost, 2)

    def run(self) -> None:
        """
        Abre o socket para que o cliente comece a sua comunicação,
        fazendo pedidos para as devidas respostas.

        :return: returns nothing
        :rtype: None
        """

        """Maintains a session with the client, following the established protocol"""
        with self._client_connection as client:
            logging.debug("Client " + str(client.peer_addr) + " just connected")
            last_request = False
            while not last_request:
                last_request = self.dispatch_request()
            logging.debug("Client " + str(client.peer_addr) + " disconnected")
            self._shared_state.remove_client(self._client_connection)
            self._shared_state.concurrent_clients.release()

    def dispatch_request(self) -> (bool, bool):
        """
        Recebe o tipo de pedido feito pelo cliente e envia para o servidor,
        de modo a receber resposta indicada para enviar de volta para o cliente.
        Retorna dois booleanos para saber se é o último pedido e
        se é para continuar a correr ou fechar o socket

        :return: Continuação da execução e do último pedido
        :rtype: (bool, bool)
        """
        request_type = self._client_connection.receive_str()
        last_request = False
        keep_running = True
        if request_type == "shape":
            self.get_shape()
        elif request_type == "grid":
            self.create_grid()
        elif request_type == "getlocked":
            self.get_locked_positions()
        elif request_type == "setlocked":
            self.set_locked_positions(self._client_connection.receive_obj())
        elif request_type == "valid":
            self.valid_space(self._client_connection.receive_obj())
        elif request_type == "clear":
            self.clear_rows(self._client_connection.receive_obj())
        elif request_type == "convert":
            self.convert_shape_format(self._client_connection.receive_obj())
        elif request_type == "lost":
            self.check_lost()
        elif request_type == "exit":
            last_request = True
            keep_running = False
        return keep_running, last_request
