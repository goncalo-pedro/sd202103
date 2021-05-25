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

        :param name:
        :param game:
        """
        self._game = game
        self._name = name
        self._points = 0
        self._active = True


# adicionados métodos para os INPUTS do jogo

    def move_left(self):
        """

        :return:
        """
        print(self._game.move_left())

    def move_right(self):
        """

        :return:
        """
        print(self._game.move_right())

    def move_down(self):
        """

        :return:
        """
        print(self._game.move_down())

    def move_up(self):
        """

        :return:
        """
        print(self._game.move_up())

    def exit(self):
        """

        :return:
        """
        self._game.exit()

    def run(self):
        """

        :return:
        """
        self.move_left()
        self.exit()

    @property
    def name(self):
        """

        :return:
        """
        return self._name

    @property
    def points(self):
        """

        :return:
        """
        return self._points

    @points.setter
    def points(self, points):
        """

        :param points:
        :return:
        """
        self._points += points


######################################################################


    # set player points

    def setPoints(self):
        """

        :return:
        """
        self.points += 1

    # reset pontuaçoes no fim do jogo

    def resetPoints(self):
        """

        :return:
        """
        self.points = 0

########################################################################


