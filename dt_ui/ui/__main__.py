import stubs
import ui
from stubs.tetris_game import TetrisGame
from ui.Button import Button
from ui.TextInput import TextBox
from ui.UI import UI
from ui.Player import Player
import pygame

done = False

pygame.font.init()

widgets = []

entry_settings = {
    "inactive_on_enter": False,
    'active': False
}

game = TetrisGame(ui.SERVER_ADDRESS, stubs.PORT)

ui_game = UI(pygame.display.set_mode((800, 700)), (800 - ui.play_width) // 2, 700 - ui.play_height, game)

name = ""


def textbox_callback(final) -> None:
    """

    :param final: texto do objeto textbox
    :return: returns nothing
    """
    print('enter pressed, textbox contains {}'.format(final))


def alternative_callback(final) -> None:
    """

    :param final: texto do objeto textbox
    :return: returns nothing
    """
    print('alternative textbox contains {}'.format(final))


def button_callback() -> None:
    """

    :return: returns nothing

    """
    global done, name, game, ui_game

    if game.create_player(name):
      done = True
    else:
        ui_game.draw_player_exists('Jogador já existe!', 40, (0, 255, 0))


def main_menu():
    """
    Main da parte do cliente, corre constroi a janela de visualização
    e corre o UI para a comunicação com o servidor.
    """

    global game, done, name, ui_game

    # see all settings help(pygooey.TextBox.__init__)

    entry = TextBox(rect=(320, 450, 150, 30), command=textbox_callback, **entry_settings)

    widgets.append(entry)

    # see all settings help(pygooey.Button.__init__)
    btn_settings = {
        "clicked_font_color": (0, 0, 0),
        "hover_font_color": (205, 195, 100),
        'font': pygame.font.Font(None, 16),
        'font_color': (255, 255, 255),
        'border_color': (0, 0, 0),
    }

    btn = Button(rect=(320, 550, 150, 50), command=button_callback, text='JOGAR', **btn_settings)
    widgets.append(btn)

    ui_game.draw_title('DISTRIBUTED TETRIS', 55, (255, 255, 255))

    ui_game.draw_text_middle('Insert Player', 35, (255, 255, 255))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.K_RETURN or event.type == pygame.QUIT:

                if game.create_player(name):
                    done = True
                else:
                    print("jogador ja existe!")

            for w in widgets:
                w.get_event(event)

            name = ""
            for caracter in entry.buffer:
              name += caracter

        for w in widgets:
            w.update()
            w.draw(ui_game.window)
        pygame.display.update()

    run = True

    while run:

        ui_game.fill()
        ui_game.draw_text_middle('Press any key to begin.', 60, (255, 255, 255))

        game.create_player(name)
        player = Player(name, game)
        ui_game.player = player
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                ui_game.run()
                run = False

    game.quit_connection(name)
    pygame.quit()


pygame.display.set_caption('Tetris')

main_menu()  # start game
