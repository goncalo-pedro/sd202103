from control_client_stubs import MathServer, SERVER_ADDRESS, PORT
from control_client_ui.client import Client


def main():
    math_server = MathServer(SERVER_ADDRESS, PORT)
    client = Client(math_server)
    client.run()


main()
