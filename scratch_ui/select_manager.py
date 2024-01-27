from .abstractions import NodeType, BlockType, SelectManagerType, SelectableObjectType


class SelectManager(SelectManagerType):
    def __init__(self) -> None:
        self.selected_object = None

    def select(self, selectable_object: SelectableObjectType) -> None:
        self.selected_object = selectable_object

    def unselect(self) -> None:
        self.selected_object = None

    def get_node(self) -> None | NodeType:
        if isinstance(self.selected_object, NodeType):
            return self.selected_object

    def get_block(self) -> None | BlockType:
        if isinstance(self.selected_object, BlockType):
            return self.selected_object

    def free(self) -> None:
        self.selected_object.remove()


select_manager = SelectManager()
