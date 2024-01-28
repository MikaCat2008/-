from __future__ import annotations

from abc import ABC, abstractmethod, abstractclassmethod

from pygame.event import EventType
from pygame.surface import SurfaceType

from scratch_api.abstractions import (
    NodeType as GameNodeType,
    BlockType as GameBlockType,
    SpriteType as GameSpriteType,
    GameObjectType as GameObjectType
)


class SlotType(ABC):
    parent_block: BlockType


class NodeSlotType(SlotType):
    node: NodeType
    parent_node: NodeType

    @abstractmethod
    def set_node(self, node: NodeType) -> None:
        ...

    @abstractmethod
    def render(self) -> SurfaceType:
        ...


class BlockSlotType(SlotType):
    blocks: list[BlockType]
    indent: bool
    game_blocks: list[GameBlockType]

    @abstractmethod
    def add(self, block: BlockType) -> None:
        ...

    @abstractmethod
    def index(self, block: BlockType) -> int:
        ...

    @abstractmethod
    def insert(self, index: int, block: BlockType) -> None:
        ...

    @abstractmethod
    def insert_before(self, block: BlockType, insertable_block: BlockType) -> None:
        ...

    @abstractmethod
    def insert_after(self, block: BlockType, insertable_block: BlockType) -> None:
        ...


class RenderableObjectType(ABC):
    coords: tuple[int, int]
    rendered: SurfaceType

    @abstractmethod
    def render(self) -> SurfaceType:
        ...


class SelectableObjectType(RenderableObjectType):
    template: TemplateType | None


class NodeType(SelectableObjectType):
    game_node: GameNodeType
    nodes: list[NodeType]
    slot: NodeSlotType
    prototype: type[NodeType]

    parent_node: NodeType | None
    parent_block: BlockType | None

    @abstractmethod
    def init(self) -> None:
        ...

    @abstractmethod
    def get_child(self, mx: int) -> tuple[NodeType, int]:
        ...

    @abstractmethod
    def remove(self) -> None:
        ...

    @abstractmethod
    def up(self, game_node: GameNodeType) -> NodeSlotType:
        ...

    @abstractclassmethod
    def set_node_manager(cls, node_manager: NodeManagerType) -> None:
        ...


class BlockType(SelectableObjectType):
    game_block: GameBlockType
    sprite: SpriteType
    slot: BlockSlotType

    slots: list[SlotType]

    @abstractmethod
    def init(self) -> None:
        ...

    @abstractmethod
    def add_block(self, game_block: BlockType, slot: int) -> BlockType:
        ...

    @abstractmethod
    def get_template_element_by_y(self, y: int) -> tuple[TemplateElementType, int, int]:        
        ...

    @abstractmethod
    def get_slot_by_coords(self, x: int, y: int) -> tuple[SlotType, int, int]:
        ...

    @abstractmethod
    def get_child(self, x: int, y: int) -> tuple[BlockType, int, int]:
        ...

    @abstractmethod
    def is_event(self) -> bool:
        ...

    @abstractmethod
    def is_iterable(self) -> bool:
        ...
        
    @abstractmethod
    def remove(self) -> None:
        ...


class SelectManagerType(ABC):
    selected_object: SelectableObjectType

    @abstractmethod
    def select(self, selectable_object: SelectableObjectType) -> None:
        ...

    @abstractmethod
    def unselect(self) -> None:
        ...

    @abstractmethod
    def get_node(self) -> NodeType | None:
        ...

    @abstractmethod
    def get_block(self) -> BlockType | None:
        ...

    @abstractmethod
    def free(self) -> None:
        ...


class NodeManagerType(ABC):
    @abstractmethod
    def create_node(self, game_node: GameNodeType) -> NodeType:
        ...

    @abstractmethod
    def create_slot(self, game_node: GameBlockType) -> NodeSlotType:
        ...


class BlockManagerType(ABC):
    @abstractmethod
    def create_block(self, game_block: GameBlockType) -> BlockType:
        ...


class SpriteManagerType(ABC):
    sprites: list[SpriteType]
    selected_sprite: SpriteType
    
    @abstractmethod
    def create_sprite(self, image: SurfaceType) -> SpriteType:
        ...


class SpriteType(ABC):
    game_sprite: GameSpriteType
    blocks: list[BlockType]

    @abstractmethod
    def add_block(self, coords: tuple[int, int], game_block: GameBlockType) -> BlockType:
        ...


class FrameType(ABC):
    screen: SurfaceType
    size: tuple[int, int]
    coords: tuple[int, int]
    frames: list[FrameType]

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def start_frames(self) -> None:
        ...

    @abstractmethod
    def update(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        ...

    @abstractmethod
    def update_frames(self, events: list[EventType], mouse_coords: tuple[int, int]) -> None:
        ...


class TemplateElementType(ABC):
    color: tuple[int, int, int]
    indent: int
    rendered: SurfaceType
    template: TemplateType

    @abstractmethod
    def render(self, sy: int = 0) -> SurfaceType:
        ...


class TemplateType(ABC):
    width: int
    color: tuple[int, int, int]
    mode: str
    template_elements: list[TemplateElementType]

    def get_surfaces(self) -> list[SurfaceType]:
        ...

    def render(self) -> SurfaceType: ...


class SpawnerType(ABC):
    coords: tuple[int, int]
    
    @abstractmethod
    def spawn(self, sprite: SpriteType) -> SelectableObjectType:
        ...

    @abstractmethod
    def render(self) -> SelectableObjectType:
        ...


class NodeSpawnerType(SpawnerType):
    node: NodeType
    game_node: GameNodeType


class BlockSpawnerType(SpawnerType):
    block: BlockType
    game_block: GameBlockType


class InputFieldType(ABC):
    @abstractmethod
    def press(self, key: str) -> None:
        ...


class InputManagerType(ABC):
    selected_field: InputFieldType

    @abstractmethod
    def update(self, selectable: NodeType) -> None:
        ...

    @abstractmethod
    def select(self) -> None:
        ...
