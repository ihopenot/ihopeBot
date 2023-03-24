from Sr import *
from TTS import *
from Chat import *

class SrFactory:
    def __init__(self) -> None:
        pass

    def build(self, config) -> BaseSr:
        match config["type"].lower():
            case "azure":
                return AzureSr(config)
            case _: 
                raise NotImplementedError

class TTSFactory():
    def __init__(self):
        pass

    def build(self, config) -> BaseTTS:
        match config["type"].lower():
            case "azure":
                return AzureTTS(config)
            case _: 
                raise NotImplementedError

class ChatFactory:
    def __init__(self) -> None:
        pass

    def build(self, config) -> BaseChat:
        match config["type"].lower():
            case "tcp":
                return TcpChat(config)