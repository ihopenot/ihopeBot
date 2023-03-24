class BaseChat:
    def __init__(self, config):
        raise NotImplementedError

    def chat(self, msg):
        raise NotImplementedError
