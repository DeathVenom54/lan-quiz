import socket

from commons import events
import asyncio
import websockets

from commons.events import Event, Opcode

client_id = ''


async def run_client():
    global client_id
    PORT = 8001

    async with websockets.connect(f'ws://localhost:{PORT}') as ws:
        async for event_raw in ws:
            event = Event.from_json(event_raw)
            if event.op == Opcode.CONNECT_ACK:
                client_id = event.id
                print(f'Connected to server with id: {client_id}')


if __name__ == '__main__':
    asyncio.run(run_client())
