import socket

from game import Piece
from sockets.sockets_mod import Socket


class TetrisGame:

    """

    Classe representativa do Stub do Cliente para possibilitar a camada de comunicação com o skeleton (através do middleware)

    """

    def __init__(self, host: str, port: int) -> None:
        """

        :param host: str
        :param port: int
        """
        super().__init__()
        self._current_connection = Socket.create_client_socket(host, port)



    def get_shape(self) -> [[]]:
        """
        A pedido do cliente, comunica com o stub que pretende obter o formato da peça para desenhar a mesma em posições na grelha.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente a resposta recebida em formato de objeto.

        :return: formato da peça em 2D
        :rtype: [[]]
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("shape")
        return self._current_connection.receive_obj()

    def create_grid(self) -> [[]]:
        """

        A pedido do cliente, comunica com o stub que pretende obter a grid de jogo.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente a resposta recebida em formato de objeto.

        :return: grelha de fundo do tabuleiro
        :rtype: [[]]

        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("grid")
        return self._current_connection.receive_obj()

    def get_locked_positions(self) -> {}:
        """
        A pedido do cliente, comunica com o stub que pretende obter o mapa contendo as "locked_positions" que representam as peças assentes no jogo.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente a resposta recebida em formato de objeto.


        :return: mapa das posições preenchidas
        :rtype: {}

        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("getlocked")
        return self._current_connection.receive_obj()

    def set_locked_positions(self, locked_positions : {}) -> None:
        """

        A pedido do cliente, comunica com o stub de modo a atualizar o mapa de "locked_positions2 que representam as peças assentes no jogo.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente a resposta recebida em formato de objeto.

        :param locked_positions: {}
        :return: returns nothing
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("setlocked")
        self._current_connection.send_obj(locked_positions)

    def valid_space(self, piece: Piece) -> {}:
        """

        :param piece: object
        :return: retorna o mapa contendo as posiçoes livre nos tabuleiro
        :rtype: {}
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("valid")
        self._current_connection.send_obj(piece)
        return self._current_connection.receive_obj()

    def clear_rows(self, grid: [[]]) -> int:
        """

        :param grid: [[]]
        :return: retorna a quantidade de linhas que foram eliminadas
        :rtype: int

        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("clear")
        self._current_connection.send_obj(grid)
        return self._current_connection.receive_int(10)

    def convert_shape_format(self, current_piece: Piece) -> Piece:
        """

        :param current_piece: Piece
        :return: retorna um novo formato para a peça depois de rodada
        :rtype: Piece
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("convert")
        self._current_connection.send_obj(current_piece)
        return self._current_connection.receive_obj()

    def check_lost(self) -> int:
        """
        :return: retorna um inteiro relativo ao caso de o jogador ter perdido (1) ou (0) no caso de ainda nao ter perdido
        :rtype: int
        """
        if self._current_connection is None:
            self.connect()
        self._current_connection.send_str("lost")
        return self._current_connection.receive_int(10)


    def connect(self) -> None:
        """

        :return: returns nothing
        """
        self._current_connection = socket.socket()



