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

        :return: posição x
        :rtype: int
        """
        return self._x

    @property
    def y(self) -> int:
        """
        Retorna a posição y da peça

        :return: posição y
        :rtype: int
        """
        return self._y

    @property
    def shape(self) -> [[]]:
        """
        Retorna o formato da peça

        :return: formato da peça
        :rtype: [[]]
        """
        return self._shape

    @property
    def color(self) -> tuple:
        """
        Retorna a cor da peça

        :return: color da peça rgb
        :rtype: tuple
        """
        return self._color

    @y.setter
    def y(self, value: int) -> None:
        """
        Altera a posição y da peça

        :param value:
        :return: returns nothing
        :rtype: None
        """
        self._y = value

    @x.setter
    def x(self, value: int) -> None:
        """
        Altera a posição x da peça

        :param value:
        :return: returns nothing
        :rtype: None
        """
        self._x = value
