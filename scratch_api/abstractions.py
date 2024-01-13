from __future__ import annotations

from abc import ABC, abstractmethod

from pygame.surface import SurfaceType


class BlockType(ABC):
    event: str
    main_block: BlockType
    parent_block: BlockType
    sprite: SpriteType
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


class NodeType(ABC):
    sprite: SpriteType
    nodes: list[NodeType]

    @abstractmethod
    def get_value(self) -> object:
        ...

    @abstractmethod
    def init(self, sprite: SpriteType) -> None:
        ...

    @abstractmethod
    def reset(self) -> None:
        ...


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


Blocks = list[BlockType]

Number = int | NumberNodeType
String = str | StringNodeType
Boolean = bool | BooleanNodeType
