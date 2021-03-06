import threading
from typing import Set, List

import sockets

import game


class SharedServerState:
    def __init__(self, jogo: game.Jogo, port: int):
        self._clients: Set[sockets.Socket] = set()
        self._keep_running: bool = True
        self._port = port
        self._jogo: game.Jogo = jogo
        self._clients_lock = threading.Lock()
        self._running_lock = threading.Lock()
        self._concurrent_clients = threading.Semaphore(game.MAX_NUMBER_OF_CONCURRENT_CLIENTS)

    def add_client(self, client_socket: sockets.Socket) -> None:
        with self._clients_lock:
            self._clients.add(client_socket)

    def remove_client(self, client_socket: sockets.Socket) -> None:
        with self._clients_lock:
            self._clients.remove(client_socket)

    def stop_server(self) -> None:
        with self._running_lock:
            self._keep_running = False

    @property
    def port(self) -> int:
        return self._port

    @property
    def keep_running(self) -> bool:
        with self._running_lock:
            return self._keep_running

    @property
    def jogo(self) -> game.Jogo:
        return self._jogo

    @property
    def concurrent_clients(self) -> threading.Semaphore:
        return self._concurrent_clients

    def clients(self) -> List[str]:
        result = []
        with self._clients_lock:
            for client_socket in self._clients:
                result.append(client_socket.peer_add)
        return result
