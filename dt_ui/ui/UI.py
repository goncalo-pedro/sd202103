from ctypes import Union

import pygame
from pygame.surface import SurfaceType

from stubs.tetris_game import TetrisGame
from ui import play_width, play_height
from ui.Player import Player


class UI:
    """
    Classe que representa todos os aspetos da UI

    """
    def __init__(self, window, top_left_x: int, top_left_y: int, game: TetrisGame):
        """

        :param window: janela de jogo
        :param top_left_x: posicao X superior esquerda da janela
        :param top_left_y: posicao Y superior esquerda da janela
        :param game: objeto to tipo Jogo
        :return: returns nothing
        :rtype None

        """
        self._player = None
        self._window = window
        self.s_width = 800
        self.s_height = 700
        self._top_left_x = top_left_x
        self._top_left_y = top_left_y
        self._game = game

    @property
    def window(self) -> Union[pygame.surface, SurfaceType]:
        """
        Retorna o objecto associado à surface.

        :return: Janela de UI
        :rtype: Union[pygame.surface, SurfaceType]
        """
        return self._window

    @property
    def top_left_x(self) -> int:
        """
        Retorna a posição X do topo esquerdo da grid (Tabuleiro)

        :return: Posição do topo esquerdo no eixo do x
        :rtype: int
        """
        return self._top_left_y

    @property
    def top_left_y(self) -> int:
        """
        Retorna a posição Y do top esquerdo da grid (Tabuleiro)

        :return: Posição do topo esquerdo no eixo do y
        :rtype: int
        """
        return self._top_left_y

    @property
    def player(self) -> Player:
        """
        Retorna o player que se encontra a utilzar o UI.

        :return: Player a jogar no momento
        :rtype: Player
        """
        return self._player

    @player.setter
    def player(self, player: str) -> None:
        """
        É definido o player, depois que o mesmo insere o nome e clica em jogar

        :param player: objeto do tipo Jogador, representa o Jogador.
        :type player: str
        :return: Object
        """
        self._player = player

    def fill(self) -> None:
        """
        Preenche o ecrã

        :return: None
        """
        self._window.fill((0, 0, 0))

    def draw_text_middle(self, text: str, size: int, color: tuple) -> None:
        """
        Escreve texto num sítio do ecrã previamente definido

        :param text: string de texto destinada a ser escrita no ecrã
        :param size: inteiro referente ao tamanho de letra
        :param color: tuplo referente à cor a utilizar (R,G,B)
        :return: returns nothing
        """

        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, True, color)

        self.window.blit(label, (
            self.top_left_x + 150 + play_width / 2 - (label.get_width() / 2),
            self.top_left_y + play_height / 2 - label.get_height() / 2))

    def draw_grid(self, row: int, col: int) -> None:
        """
        Desenha a "grelha" do tabuleiro, representando os espaços que cada bloco poderá preencher

        :param row: inteiro relativo a cada linha da grid
        :type row: int
        :param col: inteiro relativo a cada coluna da grid
        :type col: int
        :return: returns nothing
        :rtype: None
        """
        sx = self.top_left_x + 150
        sy = self.top_left_y
        for i in range(row):
            pygame.draw.line(self._window, (0, 128, 128), (sx, sy + i * 30),
                             (sx + play_width, sy + i * 30))  # horizontal lines
            for j in range(col):
                pygame.draw.line(self._window, (0, 128, 128), (sx + j * 30, sy),
                                 (sx + j * 30, sy + play_height))  # vertical lines

    def update_score(self) -> None:
        """
        Desenha e atualiza o score (e nome) do jogador. É invocado quando este completa uma linha.

        :return: returns nothing
        """
        font = pygame.font.SysFont('comicsans', 30)
        font2 = pygame.font.SysFont('comcsans', 20)

        label = font.render(self._player.name, True, (255, 255, 255))
        label2 = font2.render(str(self._player.points) + " points", True, (255, 255, 255))

        sx = self.top_left_x - 50
        sy = self.top_left_y + play_height / 2 - 50

        self.window.blit(label, (sx + 10, sy - 70))
        self.window.blit(label2, (sx + 10, sy - 40))

    def draw_next_shape(self, shape: [[]]) -> None:
        """
        Desenha no lado direito do jogo qual a próxima peça a ser gerada.

        :param shape: matrix 2D referente à forma de uma peça
        :type shape: [[]]

        :return: returns nothing
        """
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', True, (255, 255, 255))

        sx = self.top_left_x + 150 + play_width + 50
        sy = self.top_left_y + play_height / 2 - 100
        format_shape = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format_shape):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(self._window, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

        self.window.blit(label, (sx + 10, sy - 30))

    def draw_window(self, grid: [[]]) -> None:
        """
        Desenha a janela principal do jogo.

        :param grid: matrix 2D relativa à grid de jogo
        :return: returns nothing
        :rtype: None
        """
        self._window.fill((0, 0, 0))

        # Tetris Title

        font = pygame.font.SysFont('comicsans', 45)
        label = font.render('DISTRIBUTED TETRIS', True, (255, 255, 255))

        self._window.blit(label, (self.top_left_x + 150 + play_width / 2 - (label.get_width() / 2), 30))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(
                    self._window,
                    grid[i][j],
                    (self.top_left_x + 150 + j * 30, self.top_left_y + i * 30, 30, 30),
                    0
                )

        # draw grid and border
        self.draw_grid(40, 10)
        pygame.draw.rect(
            self._window,
            (255, 0, 0),
            (self.top_left_x + 150,
             self.top_left_y,
             play_width,
             play_height),
            5
        )

    def draw_title(self, text: str, size: int, color: tuple):
        """
        Desenha o título "DISTRIBUTED TETRIS" no ecrã de jogo.

        :param text: string relativa ao texto a desenhar como titulo no ecra de jogo
        :param size: inteiro relativo ao tamanho de letra a utilizar
        :param color: tuplo relativo à cor (R,G,B) a utilizar
        :return: returns nothing
        :rtype: None
        """
        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, True, color)

        self.window.blit(label, (
            self._top_left_x + play_width / 2 - (label.get_width() / 2),
            self._top_left_y - 100 + play_height / 2 - label.get_height() / 2))

    def run(self):
        """
        Onde o UI é desenhado e os diferentes pedidos para o servidor são feitos.
        """

        change_piece = False
        run = True
        current_piece = self._game.get_shape()
        next_piece = self._game.get_shape()

        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.27

        while run:
            grid = self._game.create_grid()
            locked_positions = self._game.get_locked_positions()

            fall_time += clock.get_rawtime()
            clock.tick()

            # PIECE FALLING CODE
            if fall_time / 1000 >= fall_speed:
                fall_time = 0
                current_piece.y += 1
                if not (self._game.valid_space(current_piece)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_piece.x -= 1
                        if not self._game.valid_space(current_piece):
                            current_piece.x += 1

                    elif event.key == pygame.K_RIGHT:
                        current_piece.x += 1
                        if not self._game.valid_space(current_piece):
                            current_piece.x -= 1

                    elif event.key == pygame.K_UP:
                        # rotate shape
                        current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                        if not self._game.valid_space(current_piece):
                            current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                    if event.key == pygame.K_DOWN:
                        # move shape down
                        current_piece.y += 1
                        if not self._game.valid_space(current_piece):
                            current_piece.y -= 1

            shape_pos = self._game.convert_shape_format(current_piece)

            # add piece to the grid for drawing
            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_piece.color

            # IF PIECE HIT GROUND
            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color
                self._game.set_locked_positions(locked_positions)
                current_piece = next_piece
                next_piece = self._game.get_shape()
                change_piece = False

                score_plus = self._game.clear_rows(grid)
                print("ola ", score_plus)
                # call four times to check for multiple clear rows
                if score_plus:
                    self._player.points = score_plus
                    self.update_score()

            self.draw_window(grid)
            self.draw_next_shape(next_piece)
            self.update_score()
            pygame.display.update()

            # Check if user lost
            if self._game.check_lost():
                run = False

        self.draw_text_middle("You Lost", 40, (255, 255, 255))
        pygame.display.update()
        pygame.time.delay(2000)
