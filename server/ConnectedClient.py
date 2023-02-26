import nanoid


class ConnectedClient:
    def __init__(self, websocket):
        self.id = nanoid.generate(size=6)
        self.websocket = websocket
