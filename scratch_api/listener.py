class Listener:
    event: str

    def __init__(self, event: str) -> None:
        self.event = event

    def __call__[BlockType](self, cls: type[BlockType]) -> type[BlockType]:
        cls.event = self.event

        return cls
