class BaseTTS():
    def __init__(self, config):
        raise NotImplementedError

    def speak(self, text):
        raise NotImplementedError
