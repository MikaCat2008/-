from .memory import memory


def emit(event: str, **data: dict[str, object]) -> None:
    for sprite in memory.sprites:
        sprite.emit(event, **data)
