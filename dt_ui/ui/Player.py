from stubs.tetris_game import TetrisGame


class Player:
    """

    """

################## adicionados atributos necessários para o jogador ##################

    #name = ''
    #points = 0
    #active = False
#######################################################################################


    def __init__(self, name, game: TetrisGame):
        """

        :param name: str
        :param game: object

        """
        self._game = game
        self._name = name
        self._points = 0
        self._active = True


# adicionados métodos para os INPUTS do jogo

    def move_left(self) -> None:
        """

        :return: returns nothing
        """
        print(self._game.move_left())

    def move_right(self) -> None:
        """

        :return: returns nothing
        """
        print(self._game.move_right())

    def move_down(self) -> None:
        """

        :return: returns nothing
        """
        print(self._game.move_down())

    def move_up(self) -> None:
        """

        :return: returns nothing
        """
        print(self._game.move_up())

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

        :param points: int
        :return: int
        """
        self._points += points


######################################################################


    # set player points

    def setPoints(self) -> None:
        """

        :return: returns nothing
        """
        self.points += 1

    # reset pontuaçoes no fim do jogo

    def resetPoints(self) -> None:
        """

        :return: returns nothing
        """
        self.points = 0

########################################################################


