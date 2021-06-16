from typing import List

from control_client_stubs import TetrisServer


class Client:
    def __init__(self, server: TetrisServer) -> None:
        """
        Creates a client given the control_client_stubs control_client_stubs to use
        :param math_server: The math control_client_stubs the client will use
        """
        self._server = server

    def list_cli(self) -> None:
        """
        Asks the user two integer numbers and use the control_client_stubs control_client_stubs to add them
        """
        clients: List[str] = self._server.list_clients()
        print("There are", len(clients), "clients connected on the server")
        for i, client in enumerate(clients, start=1):
            print(str(i) + ".º " + client)

    def run(self) -> None:
        """
        Executes a simple client
        """
        command: str = ""
        while command.upper() not in ["BYE", "STOP"]:
            command = input("enter a server command (list, bye, stop): ").upper()
            if command == "BYE":
                self._server.bye()
            elif command == "STOP":
                self._server.stop()
            elif command == "LIST":
                self.list_cli()
            else:
                print("Command not understood")
