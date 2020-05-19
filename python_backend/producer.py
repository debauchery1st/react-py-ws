from sys import argv
import asyncio
import websockets

async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()

if __name__ == "__main__":
    import json
    if len(argv) > 1:
        try:
            incoming = json.dumps(argv[1:])
            asyncio.run(produce(message=incoming, host='localhost', port=4000))
        except:
            asyncio.run(produce(message="error", host='localhost', port=4000))
