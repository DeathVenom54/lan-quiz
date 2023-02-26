import nanoid

# Represents a client connected to the server
class ConnectedClient:
    def __init__(self, websocket, username):
        self.id = nanoid.generate(size=6)
        self.websocket = websocket
        self.username = username
