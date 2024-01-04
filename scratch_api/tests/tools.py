from pygame.surface import Surface

from ..abstractions import NodeType, SpriteType, Blocks
from ..emit import emit
from ..block import StructureBlock
from ..memory import memory
from ..listener import Listener
from ..block_iterator import BlockIterator
from ..sprite_manager import SpriteManager

sprite_manager = SpriteManager()


@StructureBlock
@Listener("update")
class TestUpdateBlock(BlockIterator):
    start: bool
    blocks: Blocks
    
    def __init__(self, *args: tuple[Blocks]) -> None:
        super().__init__(args)

        self.start = False
        self.blocks = args[0]

    def execute(self) -> bool:
        self.start = True

        return True
    
    def iter(self) -> Blocks:
        if self.start:
            self.start = False

            return self.blocks
        return []


def sprite(
    node: NodeType, 
    x: float = 0.0,
    y: float = 0.0,
    direction: float = 0.0,
    name: str = None,
    variables: dict[str, object] = None
) -> SpriteType:
    name = name or f"Sprite {len(memory.sprites) + 1}"
    variables = variables or []

    new_sprite = sprite_manager.create_sprite(
        blocks = [TestUpdateBlock([node])],
        variable_names = list(variables),
        name = name,
        coords = (x, y),
        direction = direction,
        surface = Surface((32, 32)),
        rotate_style = 1,
    )

    memory.sprites.append(new_sprite)

    return new_sprite


def update() -> None:
    emit("update")

    ok = False

    while not ok:
        ok = True

        for sprite in memory.sprites:
            if sprite.update():
                ok = False
