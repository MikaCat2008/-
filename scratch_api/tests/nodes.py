import unittest

from . import tools

from ..nodes import NumberNode
from ..nodes import StringNode
from ..nodes import BooleanNode
from ..nodes import VariableNode


class NodesTestCase(unittest.TestCase):
    def test_number_node(self) -> None:
        node1 = NumberNode(10)
        node2 = NumberNode(0.5)
        node3 = NumberNode(NumberNode(0.2))

        self.assertEqual(int(node1), 10)
        self.assertEqual(float(node2), 0.5)
        self.assertEqual(float(node3), 0.2)

    def test_string_node(self) -> None:
        node1 = StringNode("text")
        node2 = StringNode(StringNode("text"))

        self.assertEqual(str(node1), "text")
        self.assertEqual(str(node2), "text")

    def test_boolean_node(self) -> None:
        node1 = BooleanNode(True)
        node2 = BooleanNode(BooleanNode(False))

        self.assertEqual(bool(node1), True)
        self.assertEqual(bool(node2), False)

    def test_variable_node(self) -> None:
        sprite = tools.sprite(
            variables = {
                "a": 2
            }
        )
        node = VariableNode("a")
        node.sprite = sprite

        self.assertEqual(node.get_value(), 2)
