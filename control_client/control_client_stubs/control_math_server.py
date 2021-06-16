from typing import List

import control_client_stubs
import sockets
from sockets.sockets_mod import Socket


class TetrisServer:
    """
    A math control_client_stubs stub (client side).
    """

    def __init__(self, host: str, port: int) -> None:
        super().__init__()
        self.current_connection = Socket.create_client_socket(host, port)

    def list_clients(self) -> List[str]:
        """
        List clients connected to the server.

        :return: a list with the information of the current connected clients
        """
        result: List[str] = []
        self.current_connection.send_str(control_client_stubs.LIST_CLIENTS)
        number_of_clients = self.current_connection.receive_int(sockets.INT_SIZE)
        while number_of_clients > 0:
            result.append(self.current_connection.receive_str())
            number_of_clients -= 1
        return result

    def stop(self):
        """Asks the server to terminate and closes the current connection"""
        self.current_connection.send_str(control_client_stubs.STOP_SERVER_OP)
        self.current_connection.close()

    def bye(self):
        """Close current connect with the server"""
        self.current_connection.send_str(control_client_stubs.BYE_OP)
        self.current_connection.close()
