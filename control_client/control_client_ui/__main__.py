from control_client_stubs import TetrisServer, SERVER_ADDRESS, PORT
from control_client_ui.client import Client


def main():
    math_server = TetrisServer(SERVER_ADDRESS, PORT)
    client = Client(math_server)
    client.run()


main()
