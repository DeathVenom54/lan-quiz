import json


class Event:
    def __init__(self, op: int, data):
        self.op = op
        self.data = data

    def to_json(self, format=False):
        data = dict(self.data)
        data['op'] = self.op
        return json.dumps(data, indent=(4 if format else 0))

    def get_data(self):
        return self.data

    @staticmethod
    def from_json(json_data: str):
        data = json.loads(json_data)
        op = data.pop('op')
        if op == Opcode.CONNECT_ACK:
            return EventConnectAck(data['id'])
        elif op == Opcode.IDENTIFY:
            return EventIdentify(data['id'], data['username'])
        else:
            return Event(op, data)


class EventDisconnect(Event):
    def __init__(self, id: int):
        self.id = id
        super().__init__(Opcode.DISCONNECT, self.get_data())

    def get_data(self):
        return {'id': self.id}

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        op = data.pop('op')
        return Event(op, data)

class EventConnectAck(Event):
    def __init__(self, id):
        self.id = id
        super().__init__(Opcode.CONNECT_ACK, self.get_data())

    def get_data(self):
        return {'id': self.id}

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        op = data.pop('op')
        return Event(op, data)

class EventIdentify(Event):
    def __init__(self, id, username):
        self.id = id
        self.username = username
        super().__init__(Opcode.IDENTIFY, self.get_data())

    def get_data(self):
        return {'id': self.id, 'username': self.username}

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        op = data.pop('op')
        return Event(op, data)

class Opcode:
    CONNECT_ACK = 1
    DISCONNECT = 2
    IDENTIFY = 3
