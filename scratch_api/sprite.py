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
        rotation_style: int
    ) -> None:
        self.blocks = blocks
        self.name = name
        self.coords = coords
        self.direction = direction
        self.surface = surface
        self.rendered_surface = surface
        self.rotation_style = rotation_style

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
        to_delete = []

        for block in self.blocks:
            if block.is_freeze():
                is_updated = True
                
                continue

            if block.event is None:
                block.execute()

            again = False
            is_structure = False
            is_block_updated = False
            
            while not again and not is_structure:
                if (next_block := block.next()):
                    is_updated = True
                    is_block_updated = True

                    again = not next_block.execute()
                    is_structure = next_block.is_structure

                    if again:
                        next_block.parent_block.again()
                    
                    if is_structure:
                        block.freeze(STRUCTURE_BLOCK_DELAY)
                else:
                    break

            if block.event is None and not is_block_updated:
                to_delete.append(block)

        for block in to_delete:
            self.blocks.remove(block)

        return is_updated

    def get_value(self, name: str) -> object:
        return self.variables[name].get_value()
    
    def set_value(self, variable_name: str, node: NodeType) -> None:
        self.variables[variable_name] = node

    def set_direction(self, direction: float) -> None:
        self.direction = direction % 360

    def delete(self) -> None:
        memory.sprites.remove(self)
