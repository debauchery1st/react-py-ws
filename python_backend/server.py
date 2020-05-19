import asyncio
import logging
import websockets
from websockets import WebSocketClientProtocol

logging.basicConfig(level=logging.INFO)


class Server:
    clients = set()

    async def register(self, ws: WebSocketClientProtocol) -> None:
        self.clients.add(ws)
        logging.info(f"{ws.remote_address} connects.")

    async def unregister(self, ws: WebSocketClientProtocol) -> None:
        self.clients.remove(ws)
        logging.info(f"{ws.remote_address} disconnects.")

    async def send_to_clients(self, message: str) -> None:
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    async def ws_handler(self, ws: WebSocketClientProtocol, url: str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketClientProtocol) -> None:
        async for message in ws:
            await self.send_to_clients(message)


if __name__ == "__main__":
    host = 'localhost'
    port = 4000
    server = Server()
    print(f"starting websocket server @ {host}:{port}")
    start_server = websockets.serve(server.ws_handler, host, port)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()
