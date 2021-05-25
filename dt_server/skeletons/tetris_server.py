import socket

from game import Piece
from sockets.sockets_mod import Socket
from game.Jogo import Jogo

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
        self._port = port
        self._server = jogo

    def get_shape(self) -> None:
        """
        Comunica ao jogo que pretende obter o formato da peça
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :return: returns nothing
        :rtype: None
        """
        shape = self._server.get_shape()
        self.send_obj(shape)

    def create_grid(self) -> None:
        """
        Comunica ao jogo que pretende obter o formato da grelha do jogo
        com as devidas posições ocupadas.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :return: returns nothing
        :rtype: None
        """
        grid = self._server.create_grid()
        self.send_obj(grid)

    def get_locked_positions(self) -> None:
        """
        Comunica ao jogo que pretende obter o map de posições ocupadas.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :return: returns nothing
        :rtype: None
        """
        locked_positions = self._server.get_locked_positions()
        self.send_obj(locked_positions)

    def set_locked_positions(self, locked_positions: {}) -> None:
        """
        Comunica ao jogo que pretende alterar as posições ocupadas pelas peças.

        :param locked_positions: {}
        :return: returns nothings
        :rtype: None
        """
        self._server.set_locked_positions(locked_positions)

    def valid_space(self, piece: [[]]) -> None:
        """
        Comunica ao jogo que pretende verificar se existe espaço disponível para a movimentação da peça.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :param piece: [[]]
        :return: returns nothing
        :rtype: None
        """
        valid_space = self._server.valid_space(piece)
        self.send_obj(valid_space)

    def clear_rows(self, grid: [[]]) -> None:
        """
        Comunica ao jogo que pretende verificar se existe espaço disponível para a movimentação da peça.
        Envia a resposta do jogo para o stub via middleware, em formato de inteiro.

        :param grid: [[]]
        :return: returns nothing
        :rtype None
        """
        rows_cleared = self._server.clear_rows(grid)
        self.send_int(rows_cleared, 2)

    def convert_shape_format(self, current_piece: Piece) -> None:
        """
        Comunica ao jogo que pretende converter o formato da forma da peça escolhida
        para o desenho da mesma em posições na grelha do tabuleiro.
        Envia a resposta do jogo para o stub via middleware, em formato de objeto.

        :param current_piece: Piece
        :return: returns nothing
        :rtype: None
        """
        shape = self._server.convert_shape_format(current_piece)
        self.send_obj(shape)

    def check_lost(self):
        """
        Comunica ao jogo que pretende verificar se o jogar já perdeu ou ainda continua a jogar.
        Envia a resposta do jogo para o stub via middleware, em formato de inteiro.

        :return: returns nothing
        :rtype: None
        """
        lost = self._server.check_lost()
        self.send_int(lost, 2)

    def run(self) -> None:
        """
        Abre o socket para que o cliente comece a sua comunicação,
        fazendo pedidos para as devidas respostas.

        :return: returns nothing
        :rtype: None
        """
        current_socket = socket.socket()
        current_socket.bind(('', self._port))
        current_socket.listen(1)

        keep_running = True
        while keep_running:
            self._current_connection, address = current_socket.accept()
            print("Client ", address, " just connected!")
            with self._current_connection:
                last_request = False
                while not last_request:
                    keep_running, last_request = self.dispatch_request()
                print("Client ", address, " disconnect ")
        current_socket.close()
        print("server stopped")

    def dispatch_request(self) -> (bool, bool):
        """
        Recebe o tipo de pedido feito pelo cliente e envia para o servidor,
        de modo a receber resposta indicada para enviar de volta para o cliente.
        Retorna dois booleanos para saber se é o último pedido e
        se é para continuar a correr ou fechar o socket

        :return: Continuação da execução e do último pedido
        :rtype: (bool, bool)
        """
        request_type = self.receive_str()
        last_request = False
        keep_running = True
        if request_type == "shape":
            self.get_shape()
        elif request_type == "grid":
            self.create_grid()
        elif request_type == "getlocked":
            self.get_locked_positions()
        elif request_type == "setlocked":
            self.set_locked_positions(self.receive_obj())
        elif request_type == "valid":
            self.valid_space(self.receive_obj())
        elif request_type == "clear":
            self.clear_rows(self.receive_obj())
        elif request_type == "convert":
            self.convert_shape_format(self.receive_obj())
        elif request_type == "lost":
            self.check_lost()
        elif request_type == "exit":
            last_request = True
            keep_running = False
        return keep_running, last_request


