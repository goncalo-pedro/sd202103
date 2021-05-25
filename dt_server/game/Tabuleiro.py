class Tabuleiro:
    """
        Tabuleiro é composto pelas posições ocupadas e pela grelha total do mesmo
    """

    def __init__(self):
        """
            Constrói um objeto "Tabuleiro" que representa o tabuleiro para as peças
        """
        self._locked_positions = {}
        self._grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    @property
    def locked_positions(self) -> {}:
        """
        Retorna o map de posições preenchidas

        :return: Posições preenchidas
        :rtype: {}
        """
        return self._locked_positions

    @locked_positions.setter
    def locked_positions(self, locked_positions: {}) -> None:
        """
        Altera o valor das posições preenchidas com as novas posições

        :param locked_positions: Map com as posições preenchidas pelas peças
        :type locked_positions: {}

        :return: returns nothing
        :rtype: None
        """
        self._locked_positions = locked_positions

    def create_grid(self) -> [[]]:
        """
        Retorna a grelha do tabuleiro com as devidas posições preenchidas

        :return: Grelha do tabuleiro
        :rtype: [[]]
        """
        grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in self._locked_positions:
                    c = self._locked_positions[(j, i)]
                    grid[i][j] = c
        self._grid = grid

        return grid

    def clear_rows(self, grid: [[]]) -> int:
        """
        Calcula a quantidade de rows que são limpas e retorna esse valor para o utilizador acumular os pontos

        :param grid: Matriz que representa a grelha do tabuleiro, onde as pessoas se encontram
        :type grid: [[]]

        :return: Linhas eliminadas
        :rtype: int
        """
        # need to see if row is clear the shift every other row above down one
        inc = 0
        ind = 0

        self._grid = grid
        for i in range(len(self._grid) - 1, -1, -1):
            row = self._grid[i]
            if (0, 0, 0) not in row:
                inc += 1
                # add positions to remove from locked
                ind = i
                for j in range(len(row)):
                    try:
                        del self._locked_positions[(j, i)]
                    except:
                        print()
                        raise

        if inc > 0:
            for key in sorted(list(self._locked_positions), key=lambda z: z[1])[::-1]:
                x, y = key
                if y < ind:
                    new_key = (x, y + inc)
                    self._locked_positions[new_key] = self._locked_positions.pop(key)

        return inc

    def valid_space(self, shape: [[]]) -> bool:
        """
        Verifica se existe espaço disponível para encaixar a peça para onde foi feito o movimento.

        :param shape: Matriz que representa o formato da peça
        :type shape: [[]]

        :return: Espaço disponível
        :rtype: bool
        """
        accepted_positions = [[(j, i) for j in range(10) if self._grid[i][j] == (0, 0, 0)] for i in range(20)]
        accepted_positions = [j for sub in accepted_positions for j in sub]
        formatted = self.convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_positions and pos[1] > -1:
                return False

        return True

    @staticmethod
    def convert_shape_format(shape: [[]]) -> []:
        """
        Converte o formato da forma da peça escolhida para o desenho da mesma em posições na grelha do tabuleiro.

        :param shape: Matriz que representa o formato da peça
        :type shape: [[]]

        :return: Posições do formato peça
        :rtype: []
        """
        positions = []
        format_shape = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((shape.x + j, shape.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions
