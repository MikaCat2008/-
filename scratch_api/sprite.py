from pygame.surface import SurfaceType

from .abstractions import SpriteType, NodeType, Blocks
from .nodes.NumberNode import NumberNode
from .memory import memory

from . import stamp

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
        self.rendered_coords = coords
        self.direction = direction
        self.surface = surface
        self.rendered_surface = surface
        self.rotation_style = rotation_style

        self.variables = {}

        for variable_name in variable_names:
            node = NumberNode()
            node.sprite = self

            self.set_value(variable_name, node)

    def emit(self, event: str, **data: dict[str, object]) -> None:
        for block in self.blocks:
            if block.sprite is None:
                block.sprite = self

                block.init_nodes()

            if block.event == event:
                block.execute(**data)

    def update(self) -> bool:
        is_updated = False
        to_delete = []

        for block in self.blocks:
            if block.is_freeze():
                is_updated = True
                
                continue

            again = False
            is_structure = False
            is_block_updated = False
            
            while not again and not is_structure:
                next_block = block.next()

                if next_block:
                    if next_block.main_block is None:
                        next_block.main_block = block
                    if next_block.sprite is None:
                        next_block.sprite = self

                        next_block.init_nodes()

                    is_updated = True
                    is_block_updated = True

                    again = not next_block.execute()
                    is_structure = next_block.is_structure

                    if again:
                        next_block.parent_block.again()
                    else:
                        next_block.reset_nodes()

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

    def stamp(self) -> None:
        stamp.stamp(self.rendered_surface, self.rendered_coords)
