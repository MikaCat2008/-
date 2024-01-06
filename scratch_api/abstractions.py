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
    def get_all_nodes(self) -> list[NodeType]:
        ...

    @abstractmethod
    def get_all_blocks(self) -> Blocks:
        ...

    @abstractmethod
    def ctx(self, node: NodeType) -> NodeType:
        ...

    @abstractmethod
    def set_sprite(self, sprite: SpriteType) -> None:
        ...

    @abstractmethod
    def set_main(self, main_block: BlockType) -> None:
        ...

    @abstractmethod
    def set_parent(self) -> None:
        ...

    @abstractmethod
    def freeze(self, seconds: float) -> None:
        ...    

    @abstractmethod
    def is_freeze(self) -> bool:
        ...

    @abstractmethod
    def get_sprite_by_name(self, name: str) -> SpriteType:
        ...


class SpriteType(ABC):
    blocks: Blocks
    variables: list[str]
    name: str
    coords: tuple[float, float]
    direction: float
    surface: SurfaceType
    rendered_surface: SurfaceType
    rotation_style: int

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


class NodeType(ABC):
    sprite: SpriteType

    @abstractmethod
    def get_value(self) -> object:
        ...

    @abstractmethod
    def set_sprite(self, sprite: SpriteType) -> None:
        ...


class NumberNodeType(NodeType):
    value: float


class StringNodeType(NodeType):
    value: str


class BooleanNodeType(NodeType):
    value: bool


Blocks = list[BlockType]

Number = int | NumberNodeType
String = str | StringNodeType
Boolean = bool | BooleanNodeType
