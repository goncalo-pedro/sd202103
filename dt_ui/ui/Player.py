from stubs.tetris_game import TetrisGame


class Player:
    """
        Classe representativa do Player com nome, pontos e a conexão ao servidor via socket
    """
    def __init__(self, name, game: TetrisGame):
        """
        Constrói o objeto "Player"

        :param name: Nome do jogador a jogar
        :type name: str
        :param game: Jogo ativo
        :type game: str
        """
        self._game = game
        self._name = name
        self._points = 0
        self._active = True

    @property
    def name(self) -> str:
        """
        Retorna o nome do jogador

        :return: Nome do jogador
        :rtype: str
        """
        return self._name

    @property
    def points(self) -> int:
        """
        Retorna o número de pontos do jogador

        :return: Número de pontos
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points) -> None:
        """
        Adiciona pontos ao jogador em questão.

        :param points: Inteiro dos ganhos pelo jogador
        :type points: int

        :return: returns nothings
        :rtype: None
        """
        self._points += points
