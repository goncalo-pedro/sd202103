import random

from game.Piece import Piece
from game.Tabuleiro import Tabuleiro


class Jogo:
    """
    Jogo encapsula um tabuleiro e peças
    """
    def __init__(self, tabuleiro: Tabuleiro, pecas: []):
        """
        Costrói um objeto "Jogo"
        :param tabuleiro:
        :param pecas:
        return: returns nothing
        """
        self._tabuleiro = tabuleiro
        self._pecas = pecas

    def get_shape(self):
        """

        :return:
        """
        peca = random.choice(self._pecas)
        return Piece(5, 0, peca.shape, peca.color)

    def set_locked_positions(self, locked_positions):
        """

        :param locked_positions:
        :return: returns nothing
        """
        self._tabuleiro.locked_positions = locked_positions

    def get_locked_positions(self):
        """

        :return:
        """
        return self._tabuleiro.locked_positions

    def create_grid(self):
        """

        :return:
        """
        return self._tabuleiro.create_grid()

    def clear_rows(self, grid):
        """

        :param grid:
        :return:
        """
        return self._tabuleiro.clear_rows(grid)

    def valid_space(self, shape):
        """

        :param shape:
        :return:
        """
        return self._tabuleiro.valid_space(shape)

    def convert_shape_format(self, shape):
        """

        :param shape:
        :return:
        """
        return self._tabuleiro.convert_shape_format(shape)

    def grid(self):
        """

        :return:
        """
        return self._tabuleiro

    def check_lost(self):
        """

        :return:
        """
        for pos in self._tabuleiro.locked_positions:
            x, y = pos
            if y < 1:
                self._tabuleiro.locked_positions = {}
                return True
        return False