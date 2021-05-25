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

        :param tabuleiro: Objeto que representa o Tabuleiro associado ao Jogo
        :type tabuleiro: Tabuleiro
        :param pecas: Lista de peças disponíveis no Jogo
        :type pecas: []

        :return: returns nothing
        """
        self._tabuleiro = tabuleiro
        self._pecas = pecas

    def get_shape(self) -> Piece:
        """
        Escolhe uma peça aleatória apartir da lista de peças e retorna a mesma.

        :return: Peça escolhida aleatoriamente
        :rtype: Piece
        """
        peca = random.choice(self._pecas)
        return Piece(5, 0, peca.shape, peca.color)

    def set_locked_positions(self, locked_positions: {}) -> None:
        """
        Altera o valor das posições preenchidas com as novas posições

        :param locked_positions: Map com as posições preenchidas pelas peças
        :type locked_positions: {}

        :return: returns nothing
        :rtype: None
        """
        self._tabuleiro.locked_positions = locked_positions

    def get_locked_positions(self) -> {}:
        """
        Retorna o map de posições preenchidas

        :return: Posições preenchidas
        :rtype: {}
        """
        return self._tabuleiro.locked_positions

    def create_grid(self) -> [[]]:
        """
        Cria e retorna a grid do tabuleiro

        :return: Grelha do tabuleiro
        :rtype: [[]]
        """
        return self._tabuleiro.create_grid()

    def clear_rows(self, grid: [[]]) -> int:
        """
        Calcula a quantidade de rows que são limpas e retorna esse valor para o utilizador acumular os pontos

        :param grid: Matriz que representa a grelha do tabuleiro, onde as pessoas se encontram
        :type grid: [[]]

        :return: Número de linhas eliminadas
        :rtype: int
        """
        return self._tabuleiro.clear_rows(grid)

    def valid_space(self, shape: [[]]) -> bool:
        """
        Verifica se existe espaço disponível para encaixar a peça.

        :param shape: Matriz que representa o formato da peça
        :type shape: [[]]

        :return: Espaço disponível
        :rtype: bool
        """
        return self._tabuleiro.valid_space(shape)

    def convert_shape_format(self, shape: [[]]) -> []:
        """
        Converte o formato da forma da peça escolhida para o desenho da mesma em posições na grelha do tabuleiro.

        :param shape: Matriz que representa o formato da peça
        :type shape: [[]]

        :return: Posições do formato da peça
        :rtype: []
        """
        return self._tabuleiro.convert_shape_format(shape)

    def check_lost(self) -> bool:
        """
        Verifica se as peças já ultrapassam o limite do tabuleiro,
        se sim então perdeu, caso contrário ainda não perdeu

        :return: Perdeu o jogo
        :rtype: bool
        """
        for pos in self._tabuleiro.locked_positions:
            x, y = pos
            if y < 1:
                self._tabuleiro.locked_positions = {}
                return True
        return False
