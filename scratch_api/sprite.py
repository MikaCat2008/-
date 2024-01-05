from .abstractions import SpriteType, NodeType, Blocks
from .nodes.NumberNode import NumberNode
from .memory import memory

from pygame.surface import SurfaceType

STRUCTURE_BLOCK_DELAY = 0.01


class Sprite(SpriteType):
    def __init__(
        self, 
        blocks: Blocks, 
        variable_names: list[str],
        name: str,
        coords: tuple[float, float], 
        direction: float,
        surface: SurfaceType,
        rotate_style: int
    ) -> None:
        self.blocks = blocks
        self.name = name
        self.coords = coords
        self.direction = direction
        self.surface = surface
        self.rotate_style = rotate_style

        self.variables = {}

        for variable_name in variable_names:
            node = NumberNode()
            node.set_sprite(self)

            self.set_value(variable_name, node)

    def emit(self, event: str, **data: dict[str, object]) -> None:
        for block in self.blocks:
            if block.event == event:
                block.execute(**data)

    def update(self) -> bool:
        is_updated = False

        for block in self.blocks:
            if block.is_freeze():
                is_updated = True
                
                continue
            elif block.event is None:
                continue

            again = False
            is_structure = False
            
            while not again and not is_structure:
                if (next_block := block.next()):
                    is_updated = True

                    again = not next_block.execute()
                    is_structure = next_block.is_structure

                    if again:
                        next_block.parent_block.again()
                    
                    if is_structure:
                        block.freeze(STRUCTURE_BLOCK_DELAY)
                else:
                    break

        return is_updated

    def get_value(self, name: str) -> object:
        return self.variables[name].get_value()
    
    def set_value(self, variable_name: str, node: NodeType) -> None:
        self.variables[variable_name] = node

    def delete(self) -> None:
        memory.sprites.remove(self)
