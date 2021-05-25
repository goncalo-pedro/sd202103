class Piece(object):
    """
        Piece é composta por coluna, linha, formato e a cor
    """

    def __init__(self, column: int, row: int, shape: [[]], color: tuple):
        """
        Constrói um objeto "Piece" representa uma peça

        :param column: int
        :param row: int
        :param shape: [[]]
        :param color: tuple
        """
        self._x = column
        self._y = row
        self._shape = shape
        self._color = color
        self.rotation = 0

    @property
    def x(self) -> int:
        """
        Retorna a posição x da peça

        :return:
        """
        return self._x

    @property
    def y(self) -> int:
        """
        Retorna a posição y da peça

        :return: int
        """
        return self._y

    @property
    def shape(self) -> [[]]:
        """
        Retorna o formato da peça

        :return: [[]]
        """
        return self._shape

    @property
    def color(self) -> tuple:
        """
        Retorna a cor da peça

        :return: tuple
        """
        return self._color

    @y.setter
    def y(self, value: int) -> None:
        """
        Altera a posição y da peça

        :param value:
        :return: returns nothing
        """
        self._y = value

    @x.setter
    def x(self, value: int) -> None:
        """
        Altera a posição x da peça

        :param value:
        :return: returns nothing
        """
        self._x = value
