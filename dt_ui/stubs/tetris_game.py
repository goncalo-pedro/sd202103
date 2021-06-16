import socket

from game import Piece
from sockets.sockets_mod import Socket


class TetrisGame:

    """
    Classe representativa do Stub do Cliente para possibilitar
    a camada de comunicação com o skeleton (através do middleware)
    """

    def __init__(self, host: str, port: int) -> None:
        """
        Constrói um objeto "TetrisGame"

        :param host: address da conexão
        :type host: str
        :param port: port a ser conectada
        :type port: int
        """
        super().__init__()
        self._current_connection = Socket.create_client_socket(host, port)

    def get_shape(self) -> [[]]:
        """
        A pedido do cliente, comunica com o stub que pretende obter o
        formato da peça para desenhar a mesma em posições na grelha.
        Envia o pedido para o skeleton via middleware, e devolve para o
        cliente a resposta recebida em formato de objeto.

        :return: formato da peça em 2D
        :rtype: [[]]
        """
        self._current_connection.send_str("shape")
        return self._current_connection.receive_obj()

    def create_grid(self) -> [[]]:
        """
        A pedido do cliente, comunica com o stub que pretende obter a grid de jogo.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de objeto.

        :return: grelha de fundo do tabuleiro
        :rtype: [[]]

        """
        self._current_connection.send_str("grid")
        return self._current_connection.receive_obj()

    def get_locked_positions(self) -> {}:
        """
        A pedido do cliente, comunica com o stub que pretende obter o
        mapa contendo as "locked_positions" que representam as peças assentes no jogo.
        Envia o pedido para o skeleton via middleware, e devolve para o
        cliente a resposta recebida em formato de objeto.


        :return: mapa das posições preenchidas
        :rtype: {}

        """
        self._current_connection.send_str("getlocked")
        return self._current_connection.receive_obj()

    def set_locked_positions(self, locked_positions: {}) -> None:
        """
        A pedido do cliente, comunica com o stub de modo a atualizar
        o mapa de "locked_positions2 que representam as peças assentes no jogo.
        Envia o pedido para o skeleton via middleware,
        e devolve para o cliente a resposta recebida em formato de objeto.

        :param locked_positions: dicionário contendo as posições já ocupadas por peças
        :type locked_positions: {}
        :return: returns nothing
        """
        self._current_connection.send_str("setlocked")
        self._current_connection.send_obj(locked_positions)

    def valid_space(self, piece: Piece) -> int:
        """
        A pedido do cliente, comunica com o stub que pretende obter
        a disponibilidade de espaço para a movimentação da peça.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de inteiro.

        :param piece: Peça atual a ser jogada
        :type piece: Piece

        :return: Espaço disponível
        :rtype: int
        """
        self._current_connection.send_str("valid")
        self._current_connection.send_obj(piece)
        return self._current_connection.receive_int(2)

    def clear_rows(self, grid: [[]]) -> int:
        """
        A pedido do cliente, comunica com o stub que pretende obter
        o numero de linhas eliminadas ao tê-las completo.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de inteiro.

        :param grid: Matriz que representa a grelha do tabuleiro
        :type grid: [[]]

        :return: Quantidade de linhas que foram eliminadas
        :rtype: int

        """
        self._current_connection.send_str("clear")
        self._current_connection.send_obj(grid)
        return self._current_connection.receive_int(10)

    def convert_shape_format(self, current_piece: Piece):
        """
        A pedido do cliente, comunica com o stub que pretende obter
        o novo formato depois do pedido de rotação da peça.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de objeto.

        :param current_piece: Peça atual que está sendo jogada
        :type current_piece: Piece

        :return: Novo formato para a peça depois de rodada
        :rtype: []
        """
        self._current_connection.send_str("convert")
        self._current_connection.send_obj(current_piece)
        return self._current_connection.receive_obj()

    def check_lost(self) -> int:
        """
        A pedido do cliente, comunica com o stub que pretende obter
        a resposta de se o jogo foi perdido.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de inteiro.

        :return: Inteiro relativo ao caso de o jogador ter perdido (1) ou (0) no caso de ainda nao ter perdido
        :rtype: int
        """
        self._current_connection.send_str("lost")
        return self._current_connection.receive_int(10)
