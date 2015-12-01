from enum import Enum, unique

import cPickle as pickle

@unique
class MessageType(Enum):
    report = 'report'
    exchange_params = 'exchange_params'

class Message(object):
    def __init__(self, msg, data=None):
        assert type(msg) is MessageType, "msg '{}' is not a MessageType".format(str(msg))
        self.msg = msg
        self.data = data

    def dumps(self):
        return pickle.dumps(self)

    @classmethod
    def loads(self, aMessage):
        return pickle.loads(aMessage)
