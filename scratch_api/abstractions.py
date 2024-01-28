from __future__ import annotations

from abc import ABC, abstractmethod

from pygame.surface import SurfaceType


class GameObjectType(ABC):
    sprite: SpriteType


class NodeType(GameObjectType):
    nodes: list[NodeType]
    block: BlockType
    inited: bool
    
    parent_node: NodeType

    @abstractmethod
    def get_value(self) -> object:
        ...

    @abstractmethod
    def init(self, sprite: SpriteType) -> None:
        ...

    @abstractmethod
    def replace_node(self, node_a: NodeType, node_b: NodeType) -> None:
        ...

    @abstractmethod
    def reset(self) -> None:
        ...


class BlockType(GameObjectType):
    event: str
    main_block: BlockType
    parent_block: BlockType
    parent_blocks: list[BlockType]
    is_structure: bool
    unfreeze_time: float
    nodes: list[NodeType]

    @abstractmethod
    def execute(self, **data: dict[str, object]) -> bool:
        ...

    @abstractmethod
    def next(self) -> BlockType | None:
        ...

    @abstractmethod
    def again(self) -> None:
        ...

    @abstractmethod
    def freeze(self, seconds: float) -> None:
        ...

    @abstractmethod
    def init_nodes(self) -> None:
        ...

    @abstractmethod
    def reset_nodes(self) -> None:
        ...

    @abstractmethod
    def is_freeze(self) -> bool:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...

    @abstractmethod
    def remove(self) -> None:
        ...

    @abstractmethod
    def replace_node(self, node_a: NodeType, node_b: NodeType) -> None: 
        ...

    @abstractmethod
    def get_sprite_by_name(self, name: str) -> SpriteType:
        ...


class PenType(ABC):
    sprite: SpriteType
    color: tuple[int, int, int]
    size: int
    is_down: bool

    @abstractmethod
    def stamp(self) -> None:
        ...

    @abstractmethod
    def down(self) -> None:
        ...

    @abstractmethod
    def up(self) -> None:
        ...


class SpriteType(ABC):
    blocks: Blocks
    variables: list[str]
    name: str
    coords: tuple[float, float]
    rendered_coords = tuple[float, float]
    direction: float
    surface: SurfaceType
    rendered_surface: SurfaceType
    rotation_style: int
    is_show: bool
    pen: PenType

    @abstractmethod
    def emit(self, event: str, **data: dict[str, object]) -> None:
        ...

    @abstractmethod
    def update(self) -> bool:
        ...

    @abstractmethod
    def get_value(self, name: str) -> object:
        ...

    @abstractmethod
    def set_value(self, name: str, value: NodeType) -> None:
        ...

    @abstractmethod
    def set_direction(self, direction: float) -> None:
        ...

    @abstractmethod
    def delete(self) -> None:
        ...

    @abstractmethod
    def show(self) -> None:
        ...

    @abstractmethod
    def hide(self) -> None:
        ...


class InputManagerType(ABC):
    key_map: dict[str, bool]
    key_pmap: dict[str, bool]

    @abstractmethod
    def update(self, state: bool, scancode: int) -> None:
        ...


class SpriteManagerType(ABC):
    def create_sprite(
        self, 
        blocks: Blocks = None,
        variable_names: list[str] = None,
        name: str = None,
        coords: tuple[float, float] = (0, 0),
        direction: float = 0,
        surface: SurfaceType = None,
        rotation_style: int = 2,
        is_show: bool = True
    ) -> SpriteType:
        ...


class MemoryType:
    screen: SurfaceType | None
    stamp_screen: SurfaceType | None
    sprites: list[SpriteType]
    mouse_pos: tuple[int, int]


class NumberNodeType(NodeType):
    value: float

    @abstractmethod
    def get_value(self) -> float:
        ...


class StringNodeType(NodeType):
    value: str

    @abstractmethod
    def get_value(self) -> str:
        ...


class BooleanNodeType(NodeType):
    value: bool

    @abstractmethod
    def get_value(self) -> bool:
        ...


class VariableNodeType(NumberNodeType, StringNodeType, BooleanNodeType):
    name: str


Blocks = list[BlockType]

Number = int | NumberNodeType
String = str | StringNodeType
Boolean = bool | BooleanNodeType
