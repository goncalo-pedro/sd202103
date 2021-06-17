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

    def create_player(self, name: str) -> int:
        """
        A pedido do cliente, comunica que pretende verificar se o nome do jogador é válido,
        ou seja, se está disponível para ser usado.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de inteiro.

        :param name: Nome do jogador que foi inserido na caixa de texto
        :type name: str

        :return: Se o nome é válido ou não
        :rtype: int
        """
        self._current_connection.send_str("create_player")
        self._current_connection.send_str(name)
        return self._current_connection.receive_int(2)

    def get_jogadores(self) -> {}:
        """
        A pedido do cliente, comunica que pretende verificar quantos jogadores estão a jogar de momento.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de objeto.

        :return: Retorna o mapa de jogadores que estão a jogar
        :rtype: {}
        """
        self._current_connection.send_str("get_jogadores")
        return self._current_connection.receive_obj()

    def add_points_to_player(self, name: str, points: int) -> {}:
        """
        A pedido do cliente, comunica que pretende adicionar pontos a si mesmo,
         visto que completou a linha.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de objeto.

        :param name: Nome do jogador que irá ganhar os pontos
        :type name: str

        :param points: Quantidade de pontos que o jogador ganhou ao completar linhas
        :type points: int

        :return: Retorna o dicionário de jogadores atualizado
        :rtype: {}
        """

        self._current_connection.send_str("add_points")
        self._current_connection.send_str(name)
        self._current_connection.send_int(points, 8)
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

    def check_winner(self) -> str:
        """
        A pedido do cliente, comunica com o stub que pretende verificar quem foi o vencedor da partida de tetris.
        Envia o pedido para o skeleton via middleware, e devolve para o cliente
        a resposta recebida em formato de string o nome do jogador.

        :return: O nome do vencedor, caso seja string vazia então é um empate
        :rtype: str
        """
        self._current_connection.send_str("check_winner")
        return self._current_connection.receive_str()

    def quit_connection(self, name: str) -> None:
        """
        A pedido do cliente, comunica com o stub que pretende abandonar o jogo,
        e irá ser removido do mapa de jogadores, assim como desligar a sua conexão.
        Envia o pedido para o skeleton via middleware.

        :param name: Nome do jogador
        :type name: str

        :return: returns nothing
        :rtype: None
        """
        self._current_connection.send_str("quit_connection")
        self._current_connection.send_str(name)
