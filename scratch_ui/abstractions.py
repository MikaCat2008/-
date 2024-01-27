from __future__ import annotations

from abc import ABC, abstractmethod

from pygame.event import EventType
from pygame.surface import SurfaceType

from scratch_api.node import NodeType as GameNodeType
from scratch_api.block import BlockType as GameBlockType
from scratch_api.sprite import SpriteType as GameSpriteType


class SlotType(ABC):
    parent_block: BlockType


class NodeSlotType(SlotType):
    node: NodeType

    @abstractmethod
    def render(self) -> SurfaceType:
        ...


class BlockSlotType(SlotType):
    blocks: list[BlockType]
    indent: bool
    game_blocks: list[GameBlockType]

    @abstractmethod
    def add(self, game_block: GameBlockType) -> None:
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
    ...


class NodeType(SelectableObjectType):
    game_node: GameNodeType
    nodes: list[NodeType]
    slot: NodeSlotType


class BlockType(SelectableObjectType):
    sprite: SpriteType
    slot: BlockSlotType

    slots: list[SlotType]
    template: TemplateType

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
    def get_node(self) -> None | NodeType:
        ...

    @abstractmethod
    def get_block(self) -> None | BlockType:
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
    rendered: SurfaceType
    template: TemplateType

    @abstractmethod
    def render(self, sy: int = 0) -> SurfaceType:
        ...


class TemplateType(ABC):
    width: int
    template_elements: list[TemplateElementType]

    def render(self) -> SurfaceType: ...
