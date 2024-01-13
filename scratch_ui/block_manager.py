from .abstractions import BlockType, SpriteType, BlockManagerType

from .motion import MoveBlock

from .events import OnStartBlock

from .control import RepeatBlock

from scratch_api.abstractions import BlockType as GameBlockType

from scratch_api.motion.MoveBlock import MoveBlock as MoveGameBlock

from scratch_api.events.OnStartBlock import OnStartBlock as OnStartGameBlock

from scratch_api.control.RepeatBlock import RepeatBlock as RepeatGameBlock


class BlockManager(BlockManagerType):
    def create_block(
        self,
        sprite: SpriteType,
        coords: tuple[int, int],
        game_block: GameBlockType
    ) -> BlockType:
        if isinstance(game_block, MoveGameBlock):
            block_factory = MoveBlock

        elif isinstance(game_block, OnStartGameBlock):
            block_factory = OnStartBlock

        elif isinstance(game_block, RepeatGameBlock):
            block_factory = RepeatBlock

        return block_factory(sprite, coords, game_block)


block_manager = BlockManager()
