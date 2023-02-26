import asyncio

import websockets

from commons.events import EventConnectAck
from server.ConnectedClient import ConnectedClient

connected_clients = {}


async def handler(websocket):
    client = ConnectedClient(websocket)
    connected_clients[client.id] = client
    print(f'Client connected, id: {client.id}')

    # Send CONNECT_ACK with client id
    await websocket.send(EventConnectAck(client.id).to_json())

    # Listen for events and parse them accordingly
    while True:
        try:
            event_raw = await websocket.recv()
            print('Received event ', event_raw)

        except websockets.ConnectionClosed:
            print(f'Client {client.id} disconnected')
            connected_clients.pop(client.id)
            break


async def run_server():
    PORT = 8001
    print(f'Running server on port {PORT}')
    async with websockets.serve(handler, "", PORT):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(run_server())
