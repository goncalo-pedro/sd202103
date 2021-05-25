class Piece(object):
    """

    """

    def __init__(self, column, row, shape, color):
        """

        :param column:
        :param row:
        :param shape:
        :param color:
        """
        self._x = column
        self._y = row
        self._shape = shape
        self._color = color
        self.rotation = 0  # number from 0-3

    @property
    def x(self):
        """

        :return:
        """
        return self._x

    @property
    def y(self):
        """

        :return:
        """
        return self._y

    @property
    def shape(self):
        """

        :return:
        """
        return self._shape

    @property
    def color(self):
        """

        :return:
        """
        return self._color

    @y.setter
    def y(self, value):
        """

        :param value:
        :return:
        """
        self._y = value

    @x.setter
    def x(self, value):
        """

        :param value:
        :return:
        """
        self._x = value