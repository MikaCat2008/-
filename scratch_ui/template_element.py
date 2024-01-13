from .abstractions import TemplateElementType


class TemplateElement(TemplateElementType):
    def __init__(self) -> None:
        self.color = None
        self.template = None
