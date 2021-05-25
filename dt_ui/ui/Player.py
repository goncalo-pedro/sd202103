from stubs.tetris_game import TetrisGame


class Player:
    """

    """
    def __init__(self, name, game: TetrisGame):
        """

        :param name: Nome do jogador a jogar
        :param game: Jogo ativo

        """
        self._game = game
        self._name = name
        self._points = 0
        self._active = True

    def exit(self) -> None:
        """

        :return: returns nothing
        """
        self._game.exit()

    def run(self) -> None:
        """

        :return: returns nothing
        """
        self.move_left()
        self.exit()

    @property
    def name(self) -> str:
        """

        :return: str
        """
        return self._name

    @property
    def points(self) -> int:
        """

        :return: int
        """
        return self._points

    @points.setter
    def points(self, points) -> None:
        """

        :param points: Inteiro dos pontos atuais do jogador
        :return: int
        """
        self._points += points


